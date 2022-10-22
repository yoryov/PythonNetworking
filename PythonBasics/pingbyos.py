import sys
from subprocess import PIPE, Popen
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')
    
# Main arguments
parser.add_argument("-n", dest="network", help="Network segment[For example 192.168.56]", required=True)
parser.add_argument("-t", dest="targets", help="Targets number[For example 8 (means five targets in that network)]",type=int, required=True)
parsed_args = parser.parse_args()

for ip in range(0,parsed_args.targets):

    ipAddress = parsed_args.network +'.' + str(ip)

    # Detects the Operative System and performs the command with the right parameters
    # If is Linux
    if "linux" in sys.platform: 
        output = Popen(['/bin/ping','-c 1',ipAddress],stdout = PIPE).communicate()[0]
    
    # If is Windows
    elif "win" in sys.platform:
        output = Popen(['ping','-n',str(1), ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()[0]
    
    output = output.decode('utf-8')
    
    # print("Output",output)
    if "Lost = 0" in output or "bytes from " in output:
        print("The target %s IS responding" % ipAddress)
    else:
        print("The target %s IS NOT responding" % ipAddress)
