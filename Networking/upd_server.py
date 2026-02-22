import socket

HOST = "127.0.0.1"
PORT = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    response = "How was your day?"
    responseEncoded = response.encode('utf-8')
    sock.sendto(responseEncoded, addr)
