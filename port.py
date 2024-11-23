import socket
import time
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind(('0.0.0.0', 12345))
s.listen(1)
conn, info = s.accept()
msg = conn.recv(1024)
print(msg)
if msg == b'id\r\n':
    print("62xxxxx\r\n")
    conn.send(b'Nah Id sent data back\r\n')
if msg == b'name\r\n':
    print("RESP : Happy \r\n")
    conn.send(b'Happy\r\n')
time.sleep(0.3)
s.close()
