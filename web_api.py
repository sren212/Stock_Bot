import websocket
import json
import time
import datetime
import threading

# Replace with your actual Finnhub API key
with open("key_file.txt", "r") as key_file:
    API_KEY = key_file.readline()
symbol = "AMC"

latest_price = None

def on_message(ws, message):
    global latest_price
    data = json.loads(message)
    if 'data' in data:
        latest_price = data['data'][0]['p']

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("closed")

def on_open(ws):
    print("WebSocket opened")
    # Subscribe to the stock symbol
    ws.send(json.dumps({'type': 'subscribe', 'symbol': symbol}))

def websocket_thread():
    # websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={API_KEY}",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def log_prices(file, duration, interval):
    global latest_price
    start_time = time.time()
    while time.time() - start_time < duration:
        if latest_price is not None:
            timestamp = datetime.datetime.now()
            file.write(f"{timestamp}, {symbol}, {latest_price}\n")
            file.flush()
            print(f"{timestamp}, {symbol}, {latest_price}")
        time.sleep(interval)

file_name = input("Enter file name. ")

duration = 60
interval = 5

# Start the WebSocket in a separate thread
ws_thread = threading.Thread(target=websocket_thread)
ws_thread.daemon = True
ws_thread.start()

# Log the prices to a file for 60 seconds
with open(file_name, "w") as file:
    file.write(f"{duration}, {interval}\n")
    file.write("Time, Symbol, Price\n")
    log_prices(file, duration, interval)