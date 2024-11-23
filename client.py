import socket
import time


s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))

amount = input("Please specify the amount of money and currency "
               "[Baht, US$, BTC, SGD] (e.g., 10000 USD): ")
s.send(f'{amount}\r\n'.encode())
time.sleep(0.5)
msg = s.recv(1024)
print(msg)
s.close()
