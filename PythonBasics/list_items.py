import os

"""
pwd = os.getcwd() #  retrieve the current working directory
list_directory = os.listdir(pwd) # obtain the filenames and directories
for files in list_directory: # print each directory and file founded
    print('[-]',files)
"""

for root, directories, files in os.walk(".",topdown=False):
    for file_entry in files:
        print("[-]", os.path.join(root,file_entry))
    for name in directories:
        print("[--]", name)
