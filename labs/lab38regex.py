#!/usr/bin/env python3

import urllib.request
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search the phrase: ")
phrase = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")
#if re.search(phrase, searchMe):
#    print("Found a match!")
allMatches = re.findall(phrase, searchMe)
if re.findall(phrase, searchMe):
    print(allMatches)
    print("Number of items found: " + str(len(allMatches)))
else:
    print("No match!")
