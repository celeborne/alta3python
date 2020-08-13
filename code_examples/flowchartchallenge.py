#!/usr/bin/env python3
import sys
import time

def areYou():
    ask = input("Are you a horse?\n  >>")
    if ask.lower().strip() in ("yes", "ya", "fo sho", "yup", "yep", "yuh", "aye", "sure", "indeed", "yah"):
        legs()
    elif ask.lower().strip() in ("maybe", "dunno", "iono"):
        legs()
    elif ask.lower().strip() in ("no", "nope", "neg", "negative", "nuh", "nah"):
        cooltext()
    elif ask.lower().strip() in ("q", "quit"):
        sys.exit()
    else:
        whoops()
        areYou()

def legs():
    ask1 = input("How many legs do you walk on?\n  >>")
    if ask1.lower().strip() in ("two", "2"):
        cooltext()
    elif ask1.lower().strip() in ("four", "4", "3", "three", "one", "1", "5", "five"):
        really()
    elif ask1.lower().strip() in ("q", "quit"):
        sys.exit()
    else:
        whoops()
        legs()

def really():
    ask2 = input("Really?\n  >>")
    if ask2.lower().strip() in ("no", "nope", "neg", "negative", "nuh", "nah"):
        canYou()
    elif ask2.lower().strip() in ("yes", "ya", "fo sho", "yup", "yep", "yuh", "aye", "sure", "indeed", "yah"):
        canYou()
    elif ask2.lower().strip() in ("q", "quit"):
        sys.exit()
    else:
        whoops()
        really()

def canYou():
    ask3 = input("Can you read and write?\n  >>")
    if ask3.lower().strip() in ("yes", "ya", "fo sho", "yup", "yep", "yuh", "aye", "sure", "indeed", "yah"):
        cooltext()
    elif ask3.lower().strip() in ("no", "nope", "neg", "negative", "nuh", "nah"):
        liar()
    elif ask3.lower(). strip() in ("q", "quit"):
        sys.exit()
    else:
        whoops()
        canYou()

def liar():
    ask4 = input("Liar; You're reading this...\n  >>")
    if ask4.lower().strip() in ("yes", "ya", "fo sho", "yup", "yep", "yuh", "aye", "sure", "indeed", "yah", "you got me"):
        cooltext()
    elif ask4.lower().strip() in ("q", "quit"):
        sys.exit()
    else:
        whoops()
        liar()

def cooltext():
    i=0
    x=".......You are not a horse......."
    while i<len(x) :
        print(x[i], sep="", end="", flush=True)
        sys.stdout.flush()
        i+=1
        time.sleep(0.1)

def whoops():
    print("Oops! Whatthewhat?")

def main():
    print(
            """
            Are you a horse?

            A helpful flowchart
            """
            )
areYou()

main()
