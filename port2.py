import socket
import time
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect(('192.168.1.35', 12345))
s.send(b'id\r\n')
time.sleep(0.5)
msg = s.recv(1024)
print(msg)
s.close()
