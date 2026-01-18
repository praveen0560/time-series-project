import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import datetime
import ta
from pages.utils.plotly_figure import plotly_table
from pages.utils.plotly_figure import candlestick, plotly_table,RSI,MACD,close_chart,Moving_average# Added candlestick here

st.set_page_config(
    page_title="Stock Analysis",   
    page_icon="📈",
    layout="wide",
)

st.title("Stock Analysis 📈")

st.header("Analyze stock data, visualize trends, and compute technical indicators.")

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Enter Stock Ticker", value="AAPL")

with col2:
    start_date = st.date_input("Start Date", datetime.date(today.year - 1, today.month, today.day))

with col3:
    end_date = st.date_input("End Date", datetime.date(today.year, today.month, today.day))

st.subheader(ticker)

stock = yf.Ticker(ticker)

st.header("Company Information")

st.write(stock.info.get('longBusinessSummary'))
st.write(f"**Sector:** {stock.info.get('sector')}")
st.write(f"**Full Time Employees:** {stock.info.get('fullTimeEmployees')}")
st.write(f"**Website:** {stock.info.get('website')}")

col1, col2 =st.columns(2)

with col1:
    df=pd.DataFrame(index= ['Marker Cap', 'Beta', 'Eps','PE Ratio'])
    df['']= [stock.info.get("marketCap"),stock.info.get("beta"),stock.info.get("trailingEps"),stock.info.get("trailingPE")]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width =True)

with col2:
    df = pd.DataFrame(index= [' Quick Ratio','Revenue per share','Profit Margins', 'Debt to Equity','Return on Equity'])
    df['']= [stock.info.get("quickRatio"),stock.info.get("revenuePerShare"),stock.info.get("profitMargins"),stock.info.get("debtToEquity"),stock.info.get("returnOnEquity")]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width =True)

data = yf.download(ticker, start=start_date, end=end_date)
data.columns = data.columns.get_level_values(0)

col1, col2, col3 = st.columns(3)

last_price = data['Close'].iloc[-1]
prev_price = data['Close'].iloc[-2]
daily_change = last_price - prev_price

col1.metric("Daily Change", str(round(last_price, 2)), str(round(daily_change, 2)))


last_10_df=data.tail(10).sort_index(ascending = False).round(3)
fig_df=plotly_table(last_10_df)

st.write('##### Historical Data (Last 10 Days)')
st.plotly_chart(fig_df, use_container_width =True)

col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1])

num_period = ''
with col1:
    if st.button('5D'):
        num_period = '5d'
with col2:
    if st.button('1M'):
       num_period = '1mo'
with col3:
     if st.button('6M'):
        num_period = '6mo'
with col4:
     if st.button('YTD'):
        num_period = 'ytd'
with col5:
    if st.button('1Y'):
        num_period = '1y'
with col6:
    if st.button('5Y'):
        num_period = '5y'
with col7:
     if st.button('Max'):
        num_period = 'max'

col1,col2,col3 =st.columns([1,1,4])

with col1:
    chart_type = st.selectbox('',('Candle','Line'))
with col2:
    if chart_type =='Candle':

        indicators =st.selectbox('',('RSI','MACD'))
    else:
         indicators =st.selectbox('',('RSI','MACD','Moving Average'))

ticker_ = yf.Ticker(ticker)
data1 = ticker_.history(period='max')
new_df1 = data1  # Both now point to the same data
if num_period == '':

    if chart_type == 'Candle' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width =True)
        st.plotly_chart(RSI(data1, '1y'),use_container_width =True)

    if chart_type == 'Candle' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width =True)
        st.plotly_chart(MACD(data1, '1y'),use_container_width =True)

    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width =True)
        st.plotly_chart(RSI(data1, '1y'),use_container_width =True)
    
    if chart_type == 'Line' and indicators == 'Moving Average':
        st.plotly_chart(Moving_average(data1, '1y'), use_container_width =True)
        
    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width =True)
        st.plotly_chart(RSI(data1, '1y'),use_container_width =True)

    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width =True)
        st.plotly_chart(RSI(data1, '1y'),use_container_width =True)

    if chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width =True)
        st.plotly_chart(MACD(data1, '1y'),use_container_width =True)


else:
     
    if chart_type == 'Candle' and indicators == 'RSI':
        st.plotly_chart(candlestick(new_df1, num_period), use_container_width =True)
        st.plotly_chart(RSI(new_df1, num_period),use_container_width =True)
    
    if chart_type == 'Candle' and indicators == 'MACD':
        st.plotly_chart(candlestick(new_df1, num_period), use_container_width =True)
        st.plotly_chart(MACD(new_df1, num_period),use_container_width =True)

    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(new_df1, num_period), use_container_width =True)
        st.plotly_chart(RSI(new_df1, num_period),use_container_width =True)
    
    
    if chart_type == 'Line' and indicators == 'Moving Average':
        st.plotly_chart(Moving_average(new_df1, num_period), use_container_width =True)
    
    if chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(close_chart(new_df1, num_period), use_container_width =True)
        st.plotly_chart(MACD(new_df1, num_period),use_container_width =True)

    
       

    

    

    

    

 



    

