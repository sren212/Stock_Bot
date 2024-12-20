# stock bot python file
# Noah Ripke and Suwen Ren 2024
import requests
import datetime
import time

# given the text file generated by this program, return a list of the current values
# of the last n lines
def read_curr(file, n):
    lines = file.readlines()[-n:]
    result = []
    for line in lines:
        result.append(line.split()[3])
    return result

# given data from the finnhub api, write the information to a file
def write_data(data, file, symbol):
    file.write(str(datetime.datetime.now()) + " " + str(symbol) + " ")
    file.write(str(data['c']) + " ")
    file.write(str(data['h']) + " ")
    file.write(str(data['l']) + " ")
    file.write(str(data['o']) + " ")
    file.write(str(data['pc']) + " ")
    file.write("\n")

# given a list, calculate open, close, high, and low values respectively
def candlestick(values):
    open = values[0]
    close = values[-1]
    high = open
    low = open
    for value in values:
        if value > high:
            high = value
        if value < low:
            low = value
    return [open, close, high, low]

key_file = open("key_file.txt", "r")
api_key = key_file.readline()

# look up symbol and get response
symbol = "AMC"
url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
file = open("data.txt", "a")
length = 60
interval = 5

for i in range(int(length/interval)):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        write_data(data, file, symbol)
    else:
        # print errors
        print(f"Failed to fetch data: {response.status_code}")
        print(f"Response text: {response.text}")
        break
    time.sleep(interval)

read_file = open("data.txt", "r")
last = read_curr(read_file, int(length/interval))
print(last)
candle = candlestick(last)
print(candle)

file.close()
read_file.close()