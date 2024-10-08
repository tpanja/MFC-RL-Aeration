import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.4.150', 8001))
print('Connected to socket')

msg = s.recv(1028).decode('utf-8')
print(msg)