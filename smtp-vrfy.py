#!/usr/bin/python

import socket
import sys

'''
Begin snippet for gsstyle.py, a paste-in or importable module for
output style for use in future scripts.
'''

import colorama
from colorama import Fore, Back, Style

colorama.init()

def printinfo(output):
    print Style.DIM + "[*] ",
    for field in output:
        print field,
    print Style.RESET_ALL

def printresult(output):
    print Style.BRIGHT + Fore.BLUE + "[>] ",
    for field in output:
        print field,
    print Style.RESET_ALL

def printalert(output):
    print Style.BRIGHT + Fore.RED + "[!] ",
    for field in output:
        print field,
    print Style.RESET_ALL

'''
End snippet for gsstyle.py.
'''


if len(sys.argv) != 4:
    print "Usage: ./smtp-vrfy.py <ip.addr> <port> <input_file>"
    print
    print "Example:"
    print "     # ./smtp-vrfy.py 10.11.5.14 25 usernames.txt"
    print
    sys.exit(0)

# Create a socket
printinfo(["Creating socket..."])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
printinfo(["Connecting to", sys.argv[1], "on port", sys.argv[2], "..."])
connect = s.connect((str(sys.argv[1]), int(sys.argv[2])))

# Receive the banner
printinfo(["Retrieving banner..."])
banner = s.recv(1024)
printresult([banner])

# Ingest file of usernames
with open(sys.argv[3]) as f:
    namelist = f.readlines()

# Strip escaped newlines
namelist = [x.strip('\n') for x in namelist]

printinfo(["Testing usernames in", sys.argv[3], "..."])
#for name in namelist:
#    print name

# VRFY the usernames
for name in namelist:
    if name != '':
        s.send('VRFY ' + name + '\r\n')
        result = s.recv(1024)
        if "550" not in result:
            printresult([result])

# Close the socket
printinfo(["Closing the socket..."])
s.close()

