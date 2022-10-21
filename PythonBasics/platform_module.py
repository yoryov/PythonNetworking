import platform
from platform import python_implementation, python_version,python_version_tuple

"""
Enable us to perform basic OS operations, like OS detection
"""

os = platform.system()
print("You are in a", os, "platform")

if (os == "Windows"):
    ping_command = "ping -n 1 192.168.1.1"
else:
    ping_command = "ping -c 1 192.168.1.1"

print(ping_command)

print(python_implementation())
print(python_version())