#!/usr/bin/python3

dnsfile = open("dnsservers.txt", "r") #opens file
dnslist = dnsfile.readlines() #creates list from lines in txt file
for svr in dnslist:
    print(svr, end="")
#MUST close file (dnsfile.close()) unless indentation is used to close the loop.
