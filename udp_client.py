import socket

target = "1.0.0.1"
target_port = 53

"""
UDP socket creation
       - AF_INET means use of standard IPv4 or hostname
       - SOCK_DGRAM means this will be a UDP client
"""
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sending some data to our target...
client.sendto(b"AAABBBCCC", (target, target_port))

# receiving some data from our target
data, addr = client.recvfrom(4096)
print(data.decode())

# closing connection...
client.close()
