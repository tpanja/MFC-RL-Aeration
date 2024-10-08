import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.4.28', 8002))
print('Server Created')
s.listen(5)

while True:
    s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_recv.connect(('192.168.4.150', 8001))

    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    '''clientsocket.send(bytes('Send Data', 'utf-8'))
    time.sleep(0.2)
    data = s_recv.recv(1024).decode()
    print(data)'''