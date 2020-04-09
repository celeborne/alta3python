#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def poem_responses():
    while True:
        input_one = input("\nSTOP! Ye who runs this script of me shall answer these questions three!\nFirst... WHAT... is your first input? ")
        if (input_one.lower().strip() == 'q'):
            break
        input_two = input("Hmm... indeed.\nAnd WHAT... is your second input? ")
        if (input_two.lower().strip() == 'q'):
            break
        input_three = input("I can't even...\nThird and thrice, WHAT... is your third input? ")
        if (input_three.lower().strip() == 'q'):
            break
        input_four = input("...Lied did I, and you let out a sigh. More questions, yes, I do not deny!\nWHAT... is your fourth input? ")
        if (input_four.lower().strip() == 'q'):
            break
        input_five = input("Very well. I'm starting to see it clearly, now.\nHow now, brown cow? ")
        if (input_five.lower().strip() == 'q'):
            break
        input_six = input("Aye, aye...\nWHAT is your... what number are we on now? ")
        if (input_six.lower().strip() == 'q'):
            break
        input_seven = input("Whilst thou wonder in blunder, \"How long wilst this persist?\" I have been compiling a list!\nWHAT... is your seventh input? ")
        if (input_seven.lower().strip() == 'q'):
            pass
        input_eight = input("Just a smidge longer, now, and you have done your due diligence. Answer me this, then rest, young champion.\nWouldst thou consider a dictionary for a companion? ")
#    if (input_eight.lower().strip() == 'q'):
#        break
    d = {input_one: input_two, input_three: input_four, input_five: input_six, input_seven: input_eight}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you an *.xls file, but only on one condition...")
import time
time.sleep(3)

print("You must read the questions that follow... out loud... in a goblin voice!")
time.sleep(5)

print("Quit any time by pressing q.")

while(True):
    mylistdict.append(poem_responses()) 
 #   {"IP": value, "driver": value}
    keep_going = input("\nAs if you'd had enough... Is there anything else? Enter 'q' to quit: ")
    if (keep_going.lower().strip() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
