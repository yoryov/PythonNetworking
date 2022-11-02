import socket
from socket import AF_INET, SOCK_STREAM

firstsocket = socket.socket(AF_INET, SOCK_STREAM)
firstsocket.bind(('localhost',8080))
firstsocket.listen(5)
while True:
    print('Waiting...')
    (recvsocket, address) = firstsocket.accept()
    print('HTTP request received:')
    print(recvsocket.recv(1024))
    recvsocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n<html><body><h1>secretcode</h1></body></html>",'utf-8'))
    recvsocket.close()