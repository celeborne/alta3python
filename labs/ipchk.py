#!/usr/bin/env python3

"""
Author: Luke Thompson
"""

def main():
    ipchck = input("Apply an IP Address: ")

    if ipchck == "192.168.70.1":
        print(f"Looks like the IP Address of the Gateway was set: {ipchck} This is not recommended.")
    elif ipchck:
        print(f"Looks like IP Address was set: {ipchck}")
    else:
        print("No input provided...")

main()
