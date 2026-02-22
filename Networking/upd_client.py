import socket

HOST = "127.0.0.1"
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello there"
msgEncoded = msg.encode('utf-8')
s.sendto(msgEncoded, (HOST,PORT))
data, addr = s.recvfrom(1024)
print(data)
