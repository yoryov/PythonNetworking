protocolsList = []

protocolsList.append("ftp") # 0
protocolsList.append("ssh") # 1
protocolsList.append("smtp") # 2
protocolsList.append("https")
protocolsList.append("http")

toFind = "ssh"
found = False

for i in range(len(protocolsList)):
    found = protocolsList[i] == toFind
    if found:
        break

if found:
    print("Protocol", toFind, "found at index", i+1)
else:
    print("Protocol", toFind, "not found")
