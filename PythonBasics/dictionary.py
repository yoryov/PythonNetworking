"""
Python Dictionaries

key:value is like a list or tuple but is conformed by two characteristics
The value is accessed by name and not by their index

* Each key must be unique
* A key may be data of any type
* A dictionary is not a list
* The len() function returns the number of key:value pairs in the dictionary

"""

from typing import KeysView


protocols_ports = {"ftp":21, "ssh":22, "smtp":25, "http":80}
protocols_ports2 = {"https":443, "snmp":161, "ldap":389, "ssh":22}

protocols_ports.update(protocols_ports2)
#print(type(protocols_ports.keys()))
#print(type(protocols_ports.values()))
#print(type(protocols_ports.items()))
#print(type(protocols_ports))

items = protocols_ports.values()
print(items)
protocols_ports["http"] = 8080

print(protocols_ports["http"])

protocols_ports["rdp"] = 3389

for key, value in protocols_ports.items():
    print(key, value)