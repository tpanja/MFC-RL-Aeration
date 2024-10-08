import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.4.28', 8003))
print('Server Created')
s.listen(5)

def turn_on(duration):
    clientsocket, address = s.accept()
    print('Sending message...')
    clientsocket.send(bytes('Turn On ' + str(duration), 'utf-8'))
    print('Message sent!')
    time.sleep(0.01)

def turn_off(duration):
    clientsocket, address = s.accept()
    clientsocket.send(bytes('Turn Off ' + str(duration), 'utf-8'))
    time.sleep(0.01)

def get_data():
    s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_recv.connect(('192.168.4.150', 8001))
    
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    clientsocket.send(bytes('Send Data', 'utf-8'))
    time.sleep(0.1)
    data = s_recv.recv(1024).decode().split()
    return [float(data[1]), float(data[3]), float(data[5]), float(data[7])]