Trading Guide & Stock Prediction App
A comprehensive financial analysis and prediction platform built with Streamlit. This application allows users to explore historical stock data, perform technical analysis using popular indicators, and forecast future prices using ARIMA models.

🚀 Features
1. Stock Information & Analysis
Company Overviews: Real-time retrieval of company summaries, sector information, and website links using yfinance.

Key Financial Metrics: Detailed tables showcasing Market Cap, Beta, EPS, PE Ratio, Profit Margins, and Debt-to-Equity.

Interactive Historical Charts: View stock price movements through Line or Candlestick charts with adjustable timeframes (5D, 1M, 6M, YTD, 1Y, 5Y, Max).

Technical Indicators: Integrated technical analysis tools including:

RSI (Relative Strength Index).

MACD (Moving Average Convergence Divergence).

Moving Averages (SMA 50).

2. Stock Prediction
ARIMA Forecasting: Utilizes an AutoRegressive Integrated Moving Average (ARIMA) model to predict the next 30 days of stock closing prices.

Performance Metrics: Calculates and displays the Model RMSE (Root Mean Square Error) score to evaluate prediction accuracy.

Forecast Visualization: Provides both a tabular view of predicted prices and a visual trend line for future performance.

🛠️ Project Structure
Trading_app.py: The main entry point and landing page of the application.

Stock_Analysis.py: Page dedicated to historical data visualization and technical indicators.

Stock_Prediction.py: Page focused on machine learning-based price forecasting.

pages/utils/:

model_train.py: Contains logic for data scaling, stationarity checks (ADF test), and ARIMA model training.

plotly_figure.py: Custom functions for generating interactive Plotly tables and charts.
