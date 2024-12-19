# stock bot python file
# Noah Ripke and Suwen Ren 2024
# Alpha Vantage API key: GQS16FKL9IG7JU3T
# f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
# f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

import requests

api_key = 'cthi3h1r01qtho2pjeo0cthi3h1r01qtho2pjeog'

symbol = input("Enter the symbol you want to look up.")
print(f"Looking up {symbol}...")
url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(f"Response text: {response.text}")

if 'c' in data: 
    print(f"Current price: ${data['c']}")
if 'h' in data:
    print(f"High price of the day: ${data['h']}")
if 'l' in data:
    print(f"Low price of the day: ${data['l']}")
if 'o' in data:
    print(f"Open price of the day: ${data['o']}")
if 'pc' in data:
    print(f"Previous close price: ${data['pc']}")
