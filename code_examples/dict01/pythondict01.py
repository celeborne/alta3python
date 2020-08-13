#!/usr/bin/python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])

print("First test - .get()")
print(switch.get("lynx", "The Key is in Another Castle!"))

print ("Third test - .get()")
print (switch.get("version"))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())
