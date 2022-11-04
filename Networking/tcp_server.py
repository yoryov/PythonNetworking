import socket
import threading


"""
Simple TCP Server

Establish an IP and Port to listen on

"""

IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) # ip and port to listen on
    server.listen(5) # start listening with 5 maximum connections
    print(f'[*] Listening on {IP}:{PORT}')

# Waiting for connections...
    while True:
        client, address = server.accept() # receive client socket and address
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'Hey! How are you?')
if __name__ == '__main__':
    main()