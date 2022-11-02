import streamlit as st
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas_datareader as data

from nsepy import get_history
from datetime import date
 
df = pd.read_csv('data (2).csv')

#def get_ticker(name):
   #company = finance.Ticker(name)  # google
    #return company
 
 
# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")

 
#company1 = get_ticker("GOOGL")
#company2 = get_ticker("MSFT")
 
# fetches the data: Open, Close, High, Low and Volume
#google = finance.download("GOOGL", start="2021-10-01", end="2021-10-01")
#microsoft = finance.download("MSFT", start="2021-10-01", end="2021-10-01")
 
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#data1 = company1.history(period="3mo")
#data2 = company2.history(period="3mo")
 
# markdown syntax
#st.write("""
### Google
#""")
 
# detailed summary on Google
##st.line_chart(data1.values) 
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.offline import iplot

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 


cf.go_offline()


df.iplot(kind='scatter', x='Date', y='Close',color=['gold'], 
theme='solar', mode='lines', xTitle='Date', yTitle='Close Price')

plt.show()
 
st.write("""
### Microsoft
""")
#st.write(company2.info['longBusinessSummary'], "\n", microsoft)
#st.line_chart(data2.values)