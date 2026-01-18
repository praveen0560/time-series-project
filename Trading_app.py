import streamlit as st

st.set_page_config(
    page_title="Trading App",   
    page_icon="💹",
    layout="wide",
)

st.title("Welcome to the Trading Guide💹")
st.header("We provide the Greatest platform for you to collect all the information you need to trade successfully.")

st.image("2.png")

st.markdown("## We provide the following features:")

st.markdown("### :one: Stock Information")
st.write("Throught this page, you can see all the information about stocks, including historical data, key statistics, and recent news articles.")

st.markdown("### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical data using advanced machine learning models.")

