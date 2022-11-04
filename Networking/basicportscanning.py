import socket
import sys
import errno
from datetime import datetime

target = input("Enter a target: ")
iptarget = socket.gethostbyname(target)
startport = input("Enter a start port:")
endport = input("Enter a end port: ")
time_init = datetime.now()
print("Scanning target", iptarget,"please wait...")


def PortScanner(target):
    try:
        for port in range(int(startport), int(endport)):
            connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect.settimeout(5)
            result = connect.connect_ex((target,port))
            if result == 0:
                print("[+] Port {}: \t Open".format(port))
            else:
                print("[+] Port {}: \t Closed".format(port))
                print("Reason", errno.errorcode[result])
            connect.close()
        time_finish = datetime.now()
        print("Scan completed in:", time_finish - time_init)
    except socket.error as error:
        print("[-] Connection Error!", str(error))
        sys.exit()
    
PortScanner(iptarget)
