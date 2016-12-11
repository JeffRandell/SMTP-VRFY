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

# Help section
#
if len(sys.argv) != 5:
    print "Usage: ./smtp-vrfy.py <ip.first> <ip.last> <port> <input_file>"
    print
    print "ARGUMENT        FORMAT  DESCRIPTION"
    print " <ip.first>      IPv4    First address in the range you want to test."
    print " <ip.last>       IPv4    Last address in the range you want to test."
    print " <port>          int     Destination (server) port to use. Typically 25."
    print " <input_file>    str     File with list of usernames to VRFY."
    print
    print "Ex:"
    print "  # ./smtp-vrfy.py 10.11.1.1 10.11.1.254 25 usernames.txt"
    print
    sys.exit(0)

# Define IP address variables from arguments
#
first1iter, first2iter, first3iter, first4iter = sys.argv[1].split('.')
first1iter = int(first1iter)
first2iter = int(first2iter)
first3iter = int(first3iter)
first4iter = int(first4iter)

last1, last2, last3, last4 = sys.argv[2].split('.')

# Iterate through IP address range and run script
#
while True:     #1st octet

    while True:     # 2nd octet

        while True:     # 3rd octet

            while True:     # 4th octet


               
                                # Run the script
                # Reset skip condition     <-- kludge :-/
                skip = 0

                # Current IP address
                curripv4 = str(first1iter) + "." + str(first2iter) + "." + str(first3iter) + "." + str(first4iter)

                # Creat the socket
                printinfo(["Creating socket..."])
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Connect to the server
                printinfo(["Connecting to", curripv4, "on port", sys.argv[3], "..."])
                try:
                    connect = s.connect((curripv4, int(sys.argv[3])))
                except:
                    printalert(["Cannot connect to", curripv4, "...!"])
                    printinfo(["Moving on..."])
                    skip = 1

                # Receive the banner
                if skip != 1:
                    printinfo(["Retrieving banner..."])
                    banner = s.recv(1024)
                    printresult([banner])

                # Ingest file of usernames
                if skip != 1:
                    with open(sys.argv[4]) as f:
                        namelist = f.readlines()

                # Strip escaped newlines
                if skip != 1:
                    namelist = [x.strip('\n') for x in namelist]
                    printinfo(["Testing usernames in", sys.argv[4], "..."])

                # VRFY the usernames
                if skip != 1:
                    for name in namelist:
                        if name != '':
                            s.send('VRFY ' + name + '\r\n')
                            result = s.recv(1024)
                            if "550" not in result:
                                printresult([result])

                # Close the socket
                printinfo(["Closing socket..."])
                s.close()




                if str(first4iter) == last4:     # 4th octet
                    break
                first4iter += 1

            if str(first3iter) == last3:     # 3rd octet
                break
            first3iter += 1

        if str(first2iter) == last2:     # 2nd octet
            break
        first2iter += 1

    if str(first1iter) == last1:    # 1st octet
        break
    first1iter += 1
    




'''
Keeping this section commented out as a backup in case I need to dispense with
the iterating IP-address while loops above.

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
with open(sys.argv[4]) as f:
    namelist = f.readlines()

# Strip escaped newlines
namelist = [x.strip('\n') for x in namelist]

printinfo(["Testing usernames in", sys.argv[4], "..."])
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
'''
