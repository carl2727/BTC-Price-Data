import yfinance as yf
import streamlit as st
import pandas as pd
st.write("# Bitcoin Closing Price in EURO")
tickerSymbol = "BTC-EUR"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2010-01-01", end="2020-11-03")
st.line_chart(tickerDf.Close)
