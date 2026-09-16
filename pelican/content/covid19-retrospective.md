Title: COVID-19: a brief retrospective
Date: 2026-09-16 20:30
Category: Others

In April 2020 I fitted SIR and SIR-X models to reported active COVID-19 cases. The figures below reproduce the original fitting procedure using only the data available at the time; the blue data series is extended with the subsequent [Johns Hopkins daily reports](https://github.com/CSSEGISandData/COVID-19), through 7 July 2020, the end of the original 90-day plotting window.

<a href="{static}/scripts/generate_covid19_retrospective.py" download>Download the Python script used to generate these figures.</a>

The blue points show the official number of active cases on each day, calculated in the same way as in the original post.

- **Austria:** the SIR-X fit captured the early peak and subsequent decline well.
- **Italy:** it captured the flattening, but underestimated and anticipated the peak (about 91,000 predicted versus 108,000 reported).
- **Portugal, Spain, and Belgium:** the fit captured the scale of the early plateau, but predicted a decline too soon.
- **US:** the fit failed beyond its short horizon: reported active cases continued to rise strongly after the predicted peak.

While the SIR-X model is not perfect, it is certainly much better than the SIR model.

![Portugal retrospective]({static}/images/covid19-retrospective/portugal-retrospective.png)
![Austria retrospective]({static}/images/covid19-retrospective/austria-retrospective.png)
![Italy retrospective]({static}/images/covid19-retrospective/italy-retrospective.png)
![Spain retrospective]({static}/images/covid19-retrospective/spain-retrospective.png)
![Belgium retrospective]({static}/images/covid19-retrospective/belgium-retrospective.png)
![US retrospective]({static}/images/covid19-retrospective/us-retrospective.png)
