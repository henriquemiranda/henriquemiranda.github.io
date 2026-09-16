#!/usr/bin/env python3
"""Recreate the April 2020 SIR/SIR-X figures and append later observations.

The fits use only the Johns Hopkins reports available through 7 April 2020,
exactly as the original 8 April script did. Later reports are plotted as data
only; they never enter either fit.
"""

from __future__ import annotations

import argparse
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import bisect, curve_fit, fmin


TODAY = date(2020, 4, 8)
START_DAYS = -50
END_MODEL = 90
START_FIT = 100
BETA = 0.38
R0_SIR = 1.47
R0_SIRX = 3.07
K = 0.01
K0 = 0.01

# Values returned by the countryinfo package used in the original script.
POPULATION = {
    "Portugal": 10477800,
    "Austria": 8527230,
    "Italy": 60769102,
    "Spain": 46507760,
    "Belgium": 11225469,
    "US": 319259000,
}


def sir(state, time, alpha, beta):
    susceptible, infected, recovered = state
    return [-alpha * susceptible * infected, alpha * susceptible * infected - beta * infected, beta * infected]


def sirx(state, time, alpha, beta, k0, k):
    susceptible, infected, recovered, quarantined = state
    return [
        -alpha * susceptible * infected - k0 * susceptible,
        alpha * susceptible * infected - beta * infected - k0 * infected - k * infected,
        beta * quarantined + beta * infected + k0 * susceptible,
        (k0 + k) * infected - beta * quarantined,
    ]


def report_path(historic_reports: Path, observed_reports: Path, current: date) -> Path:
    reports = historic_reports if current < TODAY else observed_reports
    return reports / f"{current:%m-%d-%Y}.csv"


def country_totals(historic_reports: Path, observed_reports: Path, country: str, current: date) -> tuple[float, float, float]:
    data = pd.read_csv(report_path(historic_reports, observed_reports, current))
    country_column = "Country_Region" if "Country_Region" in data.columns else "Country/Region"
    rows = data[data[country_column].astype(str) == country]
    return tuple(float(rows[column].sum()) for column in ("Confirmed", "Recovered", "Deaths"))


def active_series(historic_reports: Path, observed_reports: Path, country: str, start: int, stop: int) -> tuple[np.ndarray, np.ndarray]:
    days = np.arange(start, stop)
    values = []
    for offset in days:
        confirmed, recovered, deaths = country_totals(historic_reports, observed_reports, country, TODAY + timedelta(days=int(offset)))
        values.append(confirmed - recovered - deaths)
    return days, np.asarray(values)


def initial_state(historic_reports: Path, observed_reports: Path, country: str, start_day: int) -> list[float]:
    confirmed, recovered, deaths = country_totals(historic_reports, observed_reports, country, TODAY + timedelta(days=start_day))
    infected = confirmed - recovered - deaths
    susceptible = POPULATION[country] - infected - recovered
    return [susceptible, infected, recovered, 0.0]


def start_index(days: np.ndarray, values: np.ndarray) -> tuple[float, int]:
    crossing = interp1d(days, values - START_FIT)
    start = bisect(crossing, float(days.min()), float(days.max()))
    index = min(range(len(days)), key=lambda item: abs(days[item] - start))
    return start, index


def fit_sir(historic_reports: Path, observed_reports: Path, country: str) -> tuple[np.ndarray, np.ndarray]:
    days, values = active_series(historic_reports, observed_reports, country, START_DAYS, 0)
    start, index = start_index(days, values)
    susceptible, infected, recovered, quarantined = initial_state(historic_reports, observed_reports, country, int(start))
    state = [susceptible + quarantined, infected, recovered]

    def model(query, alpha, beta):
        time = np.linspace(min(query), max(query), 1000)
        _, active, _ = odeint(sir, state, time, args=(alpha, beta)).T
        return interp1d(time, active)(query)

    initial = [R0_SIR * BETA / POPULATION[country], BETA]
    parameters, _ = curve_fit(model, days[index:], values[index:], initial, bounds=([0, 0], [1, 1]), maxfev=100_000)
    prediction_days = np.linspace(int(start), END_MODEL, 1000)
    return prediction_days, model(prediction_days, *parameters)


def fit_sirx(historic_reports: Path, observed_reports: Path, country: str) -> tuple[np.ndarray, np.ndarray]:
    days, values = active_series(historic_reports, observed_reports, country, START_DAYS, 0)
    start, index = start_index(days, values)
    state = initial_state(historic_reports, observed_reports, country, int(start))

    def model(query, alpha, beta, k, k0):
        time = np.linspace(min(query), max(query), 1000)
        _, active, _, quarantined = odeint(sirx, state, time, args=(alpha, beta, k, k0)).T
        return interp1d(time, active + quarantined)(query)

    initial = [R0_SIRX * BETA / POPULATION[country], BETA, K, K0]
    parameters, _ = curve_fit(
        model,
        days[index:],
        values[index:],
        initial,
        absolute_sigma=True,
        bounds=([0, 0, 0, 0], [0.5, 0.5, 0.5, 0.5]),
        maxfev=100_000,
    )
    prediction_days = np.linspace(int(start), END_MODEL)
    return prediction_days, model(prediction_days, *parameters)


def annotate_peak(days: np.ndarray, values: np.ndarray, color: str) -> None:
    maximum_day = fmin(interp1d(days, -values), 0, disp=False)[0]
    maximum_value = -interp1d(days, -values)(maximum_day)
    plt.axvline(maximum_day, color=color)
    plt.annotate(
        f"({int(round(float(maximum_day)))},{int(round(float(maximum_value), -3))})",
        (maximum_day, max(values)),
    )


def plot_country(historic_reports: Path, observed_reports: Path, output: Path, country: str) -> None:
    plt.figure()
    plt.title(f"{country} ({TODAY:%d/%m/%Y}) (startfit:{START_FIT})")
    days, values = active_series(historic_reports, observed_reports, country, START_DAYS, END_MODEL + 1)
    plt.plot(days, values, "o-", label="data")

    sir_days, sir_values = fit_sir(historic_reports, observed_reports, country)
    sir_line, = plt.plot(sir_days, sir_values, label="SIR")
    annotate_peak(sir_days, sir_values, sir_line.get_color())

    sirx_days, sirx_values = fit_sirx(historic_reports, observed_reports, country)
    sirx_line, = plt.plot(sirx_days, sirx_values, label="SIR-X")
    annotate_peak(sirx_days, sirx_values, sirx_line.get_color())

    plt.axvline(0)
    plt.grid()
    plt.yscale("log")
    plt.ylim(10, None)
    plt.legend()
    plt.ylabel("Number of Infected")
    plt.xlabel("Days")
    output.mkdir(parents=True, exist_ok=True)
    plt.savefig(output / f"{country.lower()}-retrospective.png")
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--historic-reports", type=Path, required=True)
    parser.add_argument("--observed-reports", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for country in POPULATION:
        plot_country(args.historic_reports, args.observed_reports, args.output, country)


if __name__ == "__main__":
    main()
