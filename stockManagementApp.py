
from os import name
import streamlit as st
from datetime import date
import yfinance as yf
#from prophet import Prophet
#from prophet.plot import plot_plotly
from plotly import graph_objs as go



START = "2015-01-01"

TODAY = date.today().strftime("%Y-%m-%d")

#actual app

st.title("Stock prediction app") #title of the application

stocks = ("AAPL", "GOOG", "MSFT", "TSLA") #tuple object with popular stock names

chosenStock = st.selectbox("select data set for prediction", stocks)

numOfYears = st.slider("years of prediction", 1, 4)
actualPeriod = numOfYears * 365

@st.cache #no need to redownload data sets makes the system faster overall 
def getData(selectedStock : str):
    data = yf.download(selectedStock, START, TODAY)
    data.reset_index(inplace=True)

    return data


dataLoadState = st.text("loading data...")
data = getData(chosenStock)
dataLoadState.text("data loaded sucessfully!")

#displaying raw data 
st.subheader("Raw Data")
st.write(data.tail())

# plotting the raw data using plotly 

def plotRawData():
    figure = go.Figure()
    figure.add_trace(go.Scatter(x = data["Date"], y = data["Open"], name = "Stock open"))
    figure.add_trace(go.Scatter(x = data["Date"], y = data["Close"], name = "Stock close"))
    figure.layout.update(title_text = "Time series data", xaxis_rangeslider_visible = True)
    st.plotly_chart(figure)

plotRawData()
