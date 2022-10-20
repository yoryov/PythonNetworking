import sys
import os

"""
    The "os (operating system)" module allow us to access different
    functions depending of our OS like the:
    - filesystem
    - operating environment
    - permissions
"""

if len(sys.argv) == 2:
    filename = sys.argv[1]
    print("Searching for",filename,"...\n")
    if os.path.isfile(filename):
        print("[*]",filename,"founded!")
        exit(0)
    if not os.path.isfile(filename):
        print("[*]",filename,"not founded!")
        exit(0)
    if not os.path.isfile(filename, os.R_OK):
        print("[*] Access denied to see",filename)
        exit(0)