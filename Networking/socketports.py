import socket

# Target
ip='localhost'
port=8080

# Creating connection
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((ip,port))

# Sending data
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % ip
connection.send(request.encode())

# Receiving data
data = connection.recv(4096)
print("Data",str(bytes(data)))
print("Lenght",len(data))
print('closing the socket')
connection.close()
