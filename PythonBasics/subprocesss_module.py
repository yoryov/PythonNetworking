from asyncio import subprocess
from subprocess import call, Popen

"""
    Invoke and communicate with Python processes
"""

process = Popen(["python","--version"])
print(process.stdout())
process.terminate()
