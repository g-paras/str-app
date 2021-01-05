import matplotlib.pyplot as plt
import time

import numpy as np
import pandas as pd
import streamlit as st

st.title('''
Data Analysis: Google Stock Price
''')
st.write('''
The dataset we used in this project is *Alphabet Inc. (GOOGL) Stock Historical Prices & Data.*
Since this is a big data so we selected the last 10 years of the dataset.
''')
# reading the dataset
st.header('Load and take a look at the dataset')
df = pd.read_csv('GOOG.csv')
st.code('''
import pandas as pd
df = pd.read_csv('GOOGL.csv')
df.head()''')
st.dataframe(df.head())


st.sidebar.header('Python Dependencies Used')
st.sidebar.write('''
- Numpy
- Pandas
- Matplotlib
- Streamlit''')

st.subheader('Visualising dataset')
st.selectbox('Select Plot Type', ['line', 'Bar', 'Hist', 'Box'])
x = st.multiselect('Select the column name', [
                   'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], default=["Low"])
if st.button('Start'):
    st.bar_chart(df[x])

st.header('''
Data Manipulation (Feature Engineering)''')

st.write('''
First of all we need to check whether the data is stationary or not.

*A stationary time series is one whose statistical properties such as mean, variance, autocorrelation, etc. are all constant over time.*''')

st.write('Stationarity can be checked by adfuller test')

st.code('''
from statsmodels.tsa.stattools import adfuller

df_final = df['Close']
dftest = adfuller(df_final,autolag="AIC")
print("ADF:", dftest[0])
print("P-Value:", dftest[1])
''')
st.write('Output: ')
st.code('''
ADF: 0.5008830459040502
P-Value: 0.9848999110772098
''')

st.write('''
This data is ***not stationary*** because for starionary, 
''')
st.code('''
P-value(probability) < 0.05
ADF(test statistic) < -2.91
''')

st.line_chart(pd.concat([df['High'] + df['Close']]))

predictions = [1, 2, 3, 4]
test = [4, 5, 6, 7]
fig, ax = plt.subplots()
ax.title('x-axis')
ax.plot(predictions, label="line 1")
ax.plot(test, label="line 2")
ax.legend()
st.pyplot(fig)
