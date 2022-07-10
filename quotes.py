import yfinance as yf
import streamlit as st

st.write(""" simple stock historical quotes app!! """)

ticker = 'AMZN'

tickerData = yf.Ticker(ticker)
tickerDf = tickerData.history(period='1d', start='2022-2-1', end='2022-7-1')

st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)
st.write("""
## Avg. Daily Volume 
""")
st.line_chart(tickerDf.Volume)



