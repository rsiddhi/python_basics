import socket
from datetime import datetime
# 192.168.0.38
HOST = "127.0.0.1"
PORT = 6789
max_size = 1024

print('Strating the client at: ', datetime.now())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    messageToServer = input('Enter message to Server: ')
    messageToServerEncoded = messageToServer.encode('utf-8')
    s.send(messageToServerEncoded)
    if messageToServer == 'q':
        break;
    data = s.recv(max_size)
    if data.decode('utf-8') == 'q':
        break;
    print('At ', datetime.now(), ' server said ', data.decode('utf-8'))

s.close()
