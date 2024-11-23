import socket
import time
from datetime import datetime

COUNT = 0
EXCHANGE_RATES = {
    'Baht': {'US$': 0.029016583, 'BTC': 0.000000296648132, 'SGD': 0.039070965},
    'US$': {'Baht': 34.463052, 'BTC': 0.000010297, 'SGD': 1.3465047},
    'BTC': {'Baht': 3367637.20, 'US$': 97115.665, 'SGD': 130766.70},
    'SGD': {'Baht': 25.594453, 'US$': 0.74266358, 'BTC': 0.000007600121972},
}


def convert_currency(currency, amount):
    conversions = {}
    for key, rate in EXCHANGE_RATES[currency].items():
        conversions[key] = amount * rate
    return conversions


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)

conn, addr = s.accept()
msg = conn.recv(1024).decode()

amount, currency = msg.split()
conversions = convert_currency(currency, float(amount))

response = f"{datetime.now().strftime('%d %b %Y, %I:%M %p')}, "
response += f"{amount} {currency} = "

for currency, amount in conversions.items():
    if COUNT == 2:
        response += f"{amount:.6f} {currency}"
    else:
        response += f"{amount:.6f} {currency}, "
    COUNT += 1

conn.send(response.encode())
time.sleep(0.3)
s.close()
