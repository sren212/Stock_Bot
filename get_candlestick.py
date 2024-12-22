# given a list, calculate open, close, high, and low values respectively
def candlestick(values):
    open_price = float(values[0].split(", ")[2])
    close_price = float(values[-1].split(", ")[2])
    high = open_price
    low = open_price
    for value in values:
        price = float(value.split(", ")[2])
        if price > high:
            high = price
        if price < low:
            low = price
    return [open_price, close_price, high, low]

in_file = input("Enter input file name: ")
out_file = input("Enter output file name: ")
num = int(input("Enter the number of candles you want: "))

with open(in_file, "r") as file:
    duration, interval = [int(x) for x in file.readline().split(", ")]
    lines = file.readlines()[2:]
    num_lines = len(lines)
    
    if num_lines < 1:
        raise ValueError("Not enough data lines in the input file.")
    
sample_size = num_lines//num
if sample_size < 1:
    raise ValueError("Not enough data to create the requested number of candles.")

candles = []
for i in range(num):
    sample = lines[sample_size*i:sample_size*(i+1)]
    candles.append(candlestick(sample))

with open(out_file, "a") as write_file:
    for candle in candles:
        write_file.write(f"{candle[0]}, {candle[1]}, {candle[2]}, {candle[3]}\n")

print("Done.")