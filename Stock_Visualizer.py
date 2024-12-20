import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, date2num
from mplfinance.original_flavor import candlestick_ohlc
import datetime

data_file = "data.txt"

data = pd.read_csv(
    data_file, 
    sep=",", 
    header=None, 
    names=["date", "time", "ticker", "close", "high", "low", "open", "volume"]
)

# Add datetime column for formatting purposes
data["datetime"] = pd.to_datetime(data["date"] + " " + data["time"])

# Prepare data for candlestick plotting
data["date_num"] = data["datetime"].apply(date2num)
candlestick_data = data[["date_num", "open", "high", "low", "close"]].values

data_points = len(data)
print(data_points)
width = min(0.005, 0.005 / data_points)  # Adjust width dynamically

# Plot the candlestick chart
fig, ax = plt.subplots(figsize=(12, 6))
candlestick_ohlc(ax, candlestick_data, width=width, colorup='green', colordown='red')

# Format the x-axis with datetime
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
plt.xticks(rotation=45)
plt.title(f"Candlestick Chart for {data['ticker'].values[0]}")
plt.xlabel("Time")
plt.ylabel("Price")
plt.grid(False)
plt.tight_layout()
plt.show()