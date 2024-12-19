# Stock Indicator/Statistical Calculator
# Noah Ripke and Suwen Ren 2024

# Indicators Implemented:
# Percetange Price Change
# RSI
# SMA 30 minute, 1 hour etc.
# ATR
# Bollinger Bands
# Bullish Engulfing Candle
# Bearish Engulfing Candle
# Doji Candle

# All methods take in a data frame with Open, Close, High, Low, and Volume in 5 second intervals

import pandas as pd
import numpy as np

# Calculates the percetange change in opening prices 
def percentage_price_change(df):
    return (df['close']-df['open'])/df['open']

# Calculates Relative Strength Index over a certain period
def RSI(df_period):
    avg_gain = 0
    avg_loss = 0
    for row in df_period.iterrows():
        pc = percentage_price_change(row)
        if (pc > 0):
            avg_gain += pc
        else:
            avg_loss += np.abs(pc)
    
    avg_gain = avg_gain / len(df_period)
    avg_loss = avg_loss / len(df_period)
    rs = avg_gain / avg_loss
    
    rsi = 100 - (100/(1+rs))
    return rsi

# Calculates Simple Moving Average for a certain period
def SMA(df_period):
    return df_period['close'].mean()

def ATR(df):
    return

def bollinger_bands_upper(df):
    return

def bollinger_bands_lower(df):
    return

# Determine whether candle is bullish engulfing, 0 means no, then on a scale from (0,1] if yes
def is_bullish_engulfing_candle(current_candle, last_candle):
    # Requires that last candle is bearish, and current candle is bullish
    if (not is_bearish(last_candle)):
        return 0
    if (not is_bullish(current_candle)):
        return 0
    
    if (not (current_candle['close'] > last_candle['open'] and current_candle['open'] < last_candle['close'])):
        return 0

    return np.mean((current_candle['close']-last_candle['open'])/last_candle['open'], (last_candle['close']-current_candle['open'])/current_candle['open']) # Return the average between the percent engulfment of the current candle

# Determine whether candle is bearish engulfing, 0 means no, then on a scale from (0,1] if yes
def is_bearish_engulfing_candle(current_candle, last_candle):
    # Requires that last candle is bullish, and current candle is bearish
    if (not is_bullish(last_candle)):
        return 0
    if (not is_bearish(current_candle)):
        return 0
    
    if (not (current_candle['close'] < last_candle['open'] and current_candle['open'] > last_candle['close'])):
        return 0

    return np.mean((last_candle['open']-current_candle['close'])/current_candle['close'], (current_candle['open']-last_candle['close'])/last_candle['close']) # Return the average between the percent engulfment of the current candle

def is_doji_candle(current_candle):
    price_dif = current_candle['open']-current_candle['close']
    hl_dif = current_candle['high']-current_candle['open']
    tolerance = 0.01

    return np.abs(price_dif) <= tolerance*hl_dif

def is_bearish(current_candle):
    return current_candle['close'] < current_candle['open']

def is_bullish(current_candle):
    return current_candle['close'] >= current_candle['open']