import datetime
import time

# given the text file generated by this program, return a list of the current values
# of the last n lines
def read_curr(file, n):
    lines = file.readlines()[-n:]
    result = []
    for line in lines:
        result.append(float(line.split(", ")[2]))  # Convert price to float
    return result

# given a list, calculate open, close, high, and low values respectively
def candlestick(values):
    open_price = values[0]
    close_price = values[-1]
    high = open_price
    low = open_price
    for value in values:
        if value > high:
            high = value
        if value < low:
            low = value
    return [open_price, close_price, high, low]

in_file = input("Enter input file name: ")
out_file = input("Enter output file name: ")

with open(in_file, "r") as file:
    duration, interval = [int(x) for x in file.readline().split(", ")]
    file.readline()
    last = read_curr(file, int(duration // interval))  # Use integer division for n
    candle = candlestick(last)

with open(out_file, "a") as write_file:
    write_file.write(f"{candle[0]}, {candle[1]}, {candle[2]}, {candle[3]}\n")

print("Done.")