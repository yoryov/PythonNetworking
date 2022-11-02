import socket

target = "example.com"
ip = "93.184.216.34"

try:
    print("[*] IP from the Host: ", socket.gethostbyname(target))
    print("[*] More IPs from the Host: ", socket.gethostbyname_ex(target))
    #print("[*] Target confirmation: ", socket.gethostbyaddr(ip))
    print("[*] Fully qualified name: ", socket.getfqdn(target))
    print("[*] Target information: ", socket.getaddrinfo(target,None,0,socket.SOCK_STREAM))
except socket.error as er:
    print("[-] Connection error",str(er))