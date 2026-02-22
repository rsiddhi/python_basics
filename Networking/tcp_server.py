import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 6789
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

print('Staring the server at: ', datetime.now())
print('Waiting for the incoming connection from client...')
sock.listen(5)
client, addr = sock.accept()

while True:
    data = client.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print('At ', datetime.now(), addr, ' said ', data.decode('utf-8'))
    messageToClient = input("Enter message to Client")
    messageToClientEncoded = messageToClient.encode('utf-8')
    client.send(messageToClientEncoded)
    if messageToClient == 'q':
        break;
    
client.close()
sock.close()
                                    
    
