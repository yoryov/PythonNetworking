import socket

target_domain = '18.231.52.78'
target_port = 80
"""
TCP socket creation
    - AF_INET means use of standard IPv4 or hostname
    - SOCK_STREAM means this will be a TCP client

"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client (us) to the server (target)
client.connect((target_domain, target_port))

    # Sending some data...
client.send(b"HTTP/1.1\r\nHost:18.231.52.78\r\n\r\n")
        # Waiting to receive some data and print that response
response = client.recv(4096)
print(response.decode())

    # Close the socket
client.close()