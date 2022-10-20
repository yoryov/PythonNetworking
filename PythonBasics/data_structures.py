"""
LISTS

* How to create and manage Python lists

"""
# Creating an empty list...
protocolsList = []

# Adding some protocols with the append() function
protocolsList.append("ftp")
protocolsList.append("ssh")
protocolsList.append("smtp")
protocolsList.append("https")
protocolsList.append("http")

protocolsList.insert(0, "rdp")

# Print the list with the added protocols
print(protocolsList)

# Sorting the protocols list with the sort() function
protocolsList.sort()
print(protocolsList)

# Checking data type with the type() function
print(type(protocolsList))

# Checking how many protocols are in the list with the len() function
print(len(protocolsList))
print(protocolsList.count("https"))

# Grab a specific item position with the index() function
position = protocolsList.index("https")
position = position + 1
print("The HTTPS is at the " + str(position) + "º position")

# Removing list elements with the remove() function
protocolsList.remove("ssh")

print("Protocols scanned:")
for protocol in protocolsList:
    print(protocol)


