Title: COVID-19
Date: 2020-04-04 14:11
Category: Others

With respect to the ongoing coronavirus pandemic a lot as has been said about imposing quarantine and social distancing measures to "flatten the curve".

The curve they refer to is obtained by representing the number of people infected with the COVID-19 disease every day.
Since the real number of infected people is not known, the number of confirmed infections is the best approximation.

So how does this curve look like at the moment?
Can we predict how it will look in the future?

One way to do it is to compartment the total number of individuals in three boxes: (S)usceptible to infection, (I)nfected and (R)ecovered and use some constants to model how many people move between these compartments:

<img src="{static}/images/sir.png" style="width:80%; display: block; margin-left: auto; margin-right: auto;">

For a more detailed explanation read the Wikipedia page [here](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model)

Using the SIR model for the ongoing corona virus outbreak tends to overestimate the number of infected over time. That is because this model does not account for the quarantine. This does not even need to be a generalized quarantine, as long as the people that are known to be infected self-isolate. Hence the moto of the WHO to "Test, test, test".
A model that accounts for the quarantine is represented schematically here:

<img src="{static}/images/sirx.png" style="width:80%; display: block; margin-left: auto; margin-right: auto;">

I first read about this model [here](http://rocs.hu-berlin.de/corona/docs/forecast/model/).
They provide their own fit to the number of confirmed cases data from the Johns Hopkins University available [here](https://github.com/CSSEGISandData/COVID-19).
I wanted to see how these curves look like beyond the point where it is shown in the fits so I did my own python implementation of it.
Here are the fits for Portugal, Austria, Italy and US:
![portugal_model]({static}/images/portugal.png)
![austria_model]({static}/images/austria.png)
![italy_model]({static}/images/italy.png)
![us_model]({static}/images/us.png)

The final result depends very sensively on the day at which you start to solve the differential equations (startfit). In the plots represented above I choose different days for the different countries.
The code to generate these graphs is available [here](https://github.com/jmpcm/covid19/blob/master/get_sirx.py)

WARNING: I am by no means a specialist in these type of models or how to solve them. This data is meant for illustrative purposes only. I cannot exclude the possibility of a systematic error in the scripts and all the results shown here being wrong. If you do find such error please let me know so I can fix it. The real [experts](http://rocs.hu-berlin.de/corona/docs/forecast/results_by_country/) dont't risk making predictions of more than 7 days and the reason is that they tend to be wrong as time passes. In this work I fit all the variables of the model simultaneously, while the original authors fit only the new variables introduced in the SIR-X model with respect to the SIR.
