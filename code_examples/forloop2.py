#!/usr/bin/python3
vendors= ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
approved_vendors= ["cisco", "juniper", "big_ip"]

for x in vendors:
        print("\nThe vendor is " +x, end="")
        if x not in approved_vendors:
            print(" - Not an approved vendor.", end="")
print("\nEnd.")
