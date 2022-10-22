import subprocess
import sys

# if you want to use in Linux
# com_ping = /bin/ping
# param_ping = '-c 1'

com_ping = 'ping'
param_ping = '-n'
packet = 1
target = "nsa.gov"

p = subprocess.Popen([com_ping,param_ping,str(packet), target],shell=False, stderr=subprocess.PIPE)

out = p.stderr.read(1)
sys.stdout.write(str(out.decode('utf-8')))
sys.stdout.flush()
