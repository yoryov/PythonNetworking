"""
try:
    countlines = countchars = 0
    file = open('newfile.txt','r')
    lines = file.readlines()
    for line in lines:
        countlines += 1
        for char in line:
            countchars += 1
    file.close()
    print("Characters in file: ", countchars)
    print("Lines in file: ", countlines)
except IOError as error:
    print("I/O error ocurred:", str(error))
"""
try:
    myfile = open("newfile2.txt", 'wt','r')
    for i in range(10):
        myfile.write("line #1" + str(i+1) + "\n")
    myfile.readlines()
    myfile.close()
except IOError as error:
    print("I/O error ocurred:", str(error))