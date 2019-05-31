from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

dfx = pd.read_excel("a.xlsx", sheetname="EVDS")

df = dfx[:108]
dfa = dfx[-1:]

date= df["Tarih"].to_frame()
german_tourist = df["ALMANYA"].to_frame()
ıng_tourist = df["INGILTERE"].to_frame()
rus_tourist = df["RUSYA"].to_frame()
euro = df["Euro"].to_frame()
sterlin = df['Sterlin'].to_frame()
ruble = df['Ruble'].to_frame()
today_euro = dfa["Euro"].to_frame()
today_sterlin = dfa['Sterlin'].to_frame()
today_ruble = dfa['Ruble'].to_frame()
lr = LinearRegression()

def predict_german():
    lr.fit(euro,german_tourist)
    prediction_german = lr.predict(today_euro)
    print("Prediction for German tourist for todays exchange rate is: ")
    print(prediction_german)  
    print("Correlation between exchange rate and number of tourist of Germany is :")
    print( df[['Euro','ALMANYA']].corr())
    print("Covariance between exchange rate and number of tourist of Germany is : ")
    print( df[['Euro','ALMANYA']].cov())
    plt.plot(euro,german_tourist)
    plt.show()
    return prediction_german
    

def predict_ing():
    lr.fit(sterlin,ıng_tourist)
    prediction_ing = lr.predict(today_sterlin)    
    plt.plot(sterlin,ıng_tourist)
    plt.show()
    print("Prediction for British tourist for todays exchange rate is: ")
    print(prediction_ing)
    print("Correlation between exchange rate and number of tourist of England is :")
    print( df[['Sterlin','INGILTERE']].corr())
    print("Covariance between exchange rate and number of tourist of England is : ")
    print( df[['Euro','ALMANYA']].cov())
    return prediction_ing

def predict_rus():
    lr.fit(ruble,rus_tourist)
    prediction_rus = lr.predict(today_ruble)
    plt.plot(ruble,rus_tourist)
    plt.show()
    print("Prediction for Russian tourist for todays exchange rate is: ")
    print(prediction_rus)
    print("Correlation between exchange rate and number of tourist of Russia is :")
    print( df[['Ruble','RUSYA']].corr())
    print("Covariance between exchange rate and number of tourist of Russia is : ")
    print( df[['Euro','ALMANYA']].cov())
    return prediction_rus

predict_german()
predict_ing()
predict_rus()











