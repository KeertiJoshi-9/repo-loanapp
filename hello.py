import streamlit as st

st.title("This is a test title.")

st.header("This is a test header")
st.subheader("This is a test subtitle")

st.write("Write simething!!!")

st.text("This is a test paragraph.")

st.markdown("This is a **bold** text.")

import yfinance as yf

tick_data = yf.Ticker("MSFT")
tdf = tick_data.history(period='1d', start_date='2023-01-01', end_date = '2024-01-01')

st.dataframe(tdf)
