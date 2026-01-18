import plotly.graph_objects as go
import dateutil
import pandas_ta as pta
import datetime

def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e1efff'
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b></b>"] + ["<b>" + str(i)[:10] + "</b>" for i in dataframe.columns],
            line_color="#617286",
            fill_color="#2f3741",
            align='center',
            font=dict(color='white', size=15),
            height=35
        ), # Added this comma
        cells=dict(
            values=[["<b>"+str(i)+"</b>" for i in dataframe.index]] + [dataframe[i] for i in dataframe.columns],
            fill_color=[[rowOddColor, rowEvenColor] * len(dataframe)], # Added comma
            align='left',
            line_color='white',
            font=dict(color="black", size=15)
        )
    )])
    
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
    return fig

def fliter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months =-1)
    elif  num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif  num_period == '6mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months =-6)
    elif  num_period == '1Y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years =-1)
    elif  num_period == '5Y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years =-5)
    elif  num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year,1,1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index[0]
    
    return dataframe.reset_index() [dataframe.reset_index()['Date']>date]


def close_chart(dataframe, num_period = False):
    if num_period:
            dataframe = fliter_data(dataframe,num_period)
    fig= go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
                        mode='lines',
                        name='Open',line = dict(width = 2, color = '#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
                        mode='lines',
                        name='Close',line = dict(width = 2, color ='green')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
                        mode='lines',name='High',line = dict(width = 2, color = '#0078ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
                        mode='lines',name='Low',line = dict(width = 2, color = 'red')))
    fig.update_xaxes(rangeslider_visible =True)
    fig.update_layout(height=500, margin =dict(l=0,r=20,t=20,b=0), plot_bgcolor = 'black',paper_bgcolor='black',legend =dict(
    yanchor ="top",
    xanchor="right"
    )) 
    return fig

def candlestick(dataframe, num_period):
    dataframe = fliter_data(dataframe, num_period) # Fixed typo: fliter -> filter
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=dataframe['Date'],
        open=dataframe['Open'],
        high=dataframe['High'],
        low=dataframe['Low'],
        close=dataframe['Close'] 
    ))
    
    fig.update_layout(
        showlegend=False, 
        height=500, 
        margin=dict(l=0, r=20, t=20, b=0), 
        plot_bgcolor='black', 
        paper_bgcolor="#05101b"
    )
    
    return fig # Added this line

def RSI(dataframe, num_period):
    # 1. Calculate RSI (Ensure pta/pandas_ta is imported as pta)
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    
    # 2. Filter data (Fixed typo: fliter -> filter)
    dataframe = fliter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    # RSI Line
    fig.add_trace(go.Scatter(
        x=dataframe.index, # Using index is safer for yfinance dates
        y=dataframe['RSI'], 
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange'),
    ))
    
    # Overbought Line (70)
    fig.add_trace(go.Scatter(
        x=dataframe.index,
        y=[70]*len(dataframe), 
        name='Overbought', 
        marker_color='red',
        line=dict(width=2, color='red', dash='dash'),
    ))
    
    # Oversold Line (30) - Fixed the extra quote here
    fig.add_trace(go.Scatter(
        x=dataframe.index,
        y=[30]*len(dataframe), 
        fill='tonexty',
        name='Oversold', 
        marker_color="#818581",
        line=dict(width=2, color='#79da84', dash='dash'),
    ))

    fig.update_layout(
        height=300,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='black',
        paper_bgcolor="#040b13"
    )
    
    return fig # Added this to return the chart
    

def Moving_average(dataframe, num_period):
    # 1. Calculate Simple Moving Average
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], length=50)
    
    # 2. Fix typo: filter_data (not fliter_data)
    dataframe = fliter_data(dataframe, num_period)
    
    fig = go.Figure()

    # Use dataframe.index if your dates are in the index (standard for yfinance)
    # If you have a column named 'Date', keep x=dataframe['Date']
    x_axis = dataframe.index 

    fig.add_trace(go.Scatter(x=x_axis, y=dataframe['Open'],
                        mode='lines',
                        name='Open', line=dict(width=2, color='#5ab7ff')))
    
    fig.add_trace(go.Scatter(x=x_axis, y=dataframe['Close'],
                        mode='lines',
                        name='Close', line=dict(width=2, color='green')))
    
    fig.add_trace(go.Scatter(x=x_axis, y=dataframe['High'],
                        mode='lines', name='High', line=dict(width=2, color='#0078ff')))
    
    fig.add_trace(go.Scatter(x=x_axis, y=dataframe['Low'],
                        mode='lines', name='Low', line=dict(width=2, color='red')))
    
    fig.add_trace(go.Scatter(x=x_axis, y=dataframe['SMA_50'],
                        mode='lines', name='SMA 50', line=dict(width=2, color='purple')))
    
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=500, 
        margin=dict(l=0, r=20, t=20, b=0), 
        plot_bgcolor='black',
        paper_bgcolor="#090d11",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    ) 
    return fig

def MACD(dataframe, num_period):
    # 1. Calculate MACD
    macd_data = pta.macd(dataframe['Close'])
    dataframe['MACD'] = macd_data.iloc[:, 0]
    dataframe['MACD_Signal'] = macd_data.iloc[:, 1]
    dataframe['MACD_Hist'] = macd_data.iloc[:, 2]

    # 2. Filter data (Fixed typo: filter_data)
    dataframe = fliter_data(dataframe, num_period)
    
    fig = go.Figure()

    # 3. Add MACD Line
    fig.add_trace(go.Scatter(
        x=dataframe.index,
        y=dataframe['MACD'], 
        name='MACD',
        line=dict(width=2, color='blue')
    ))

    # 4. Add Signal Line
    fig.add_trace(go.Scatter(
        x=dataframe.index,
        y=dataframe['MACD_Signal'], 
        name='Signal',
        line=dict(width=2, color='orange', dash='dot')
    ))

    # 5. Add Histogram (Green for positive, Red for negative)
    colors = ['green' if val >= 0 else 'red' for val in dataframe['MACD_Hist']]
    fig.add_trace(go.Bar(
        x=dataframe.index,
        y=dataframe['MACD_Hist'],
        name='Histogram',
        marker_color=colors
    ))

    fig.update_layout(
        height=250,
        plot_bgcolor='black',
        paper_bgcolor="#060b11",
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )            
    return fig


def Moving_average_forecast(forecast):
    fig = go.Figure()

    # Only plotting the future/predicted section (last 31 points)
    fig.add_trace(go.Scatter(
        x=forecast.index[-31:], 
        y=forecast['Close'].iloc[-31:],
        mode='lines',
        name='Future Close Price',
        line=dict(width=3, color='red') # Increased width for visibility
    ))

    # Layout settings
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        height=500, 
        margin=dict(l=0, r=20, t=20, b=0), 
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color="white"), # Added to make text visible on black
        legend=dict(
            yanchor="top",
            xanchor="right",
        )
    )
    
    return fig
                            
                            