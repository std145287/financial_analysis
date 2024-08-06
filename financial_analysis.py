import streamlit as st
import yfinance as yf
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="your_api_key_here")

# Function to fetch stock data
def get_stock_data(ticker, start_date='2024-01-01', end_date='2024-02-01'):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Sidebar for user inputs
st.sidebar.header('User Input Options')
selected_stock1 = st.sidebar.text_input('Enter Stock Ticker 1', 'AAPL').upper()
selected_stock2 = st.sidebar.text_input('Enter Stock Ticker 2', 'GOOG').upper()

# Fetch stock data
stock_data1 = get_stock_data(selected_stock1)
stock_data2 = get_stock_data(selected_stock2)

# Display stock data
st.title('Interactive Financial Stock Market Comperative Analysis Tool')

col1, col2 = st.columns(2)
with col1:
    st.subheader(f"Displaying data for: {selected_stock1}")
    st.write(stock_data1)
    chart_type = st.sidebar.selectbox(f'Select Chart Type for {selected_stock1}', ['Line', 'Bar'])
    if chart_type == 'Line':
        st.line_chart(stock_data1['Close'])
    elif chart_type == 'Bar':
        st.bar_chart(stock_data1['Close'])
with col2:
    st.subheader(f"Displaying data for: {selected_stock2}")
    st.write(stock_data2)
    chart_type2 = st.sidebar.selectbox(f'Select Chart Type for {selected_stock2}', ['Line', 'Bar'])
    if chart_type2 == 'Bar':
        st.bar_chart(stock_data2['Close'])
    elif chart_type2 == 'Line':
        st.line_chart(stock_data2['Close'])