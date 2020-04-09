#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def poem_responses():
    input_one = input("\nSTOP! Ye who runs this script of me shall answer these questions three! First... WHAT... is your first input? ")
    input_two = input("Hmm... indeed. And WHAT... is your second input? ")
    input_three = input("I can't even... third and thrice, WHAT... is your third input? ")
    input_four = input("...Lied did I, and you let out a sigh. More questions, yes, I do not deny! WHAT... is your fourth input? ")
    input_five = input("Very well. I'm starting to see it clearly, now. How now, brown cow? ")
    input_six = input("Aye, aye... WHAT is your... what number are we on now? ")
    input_seven = input("You wonder in blunder, \"How long wilst this persist?\" ")
    input_eight = input("Just a smidge longer, now, and you have done your due diligence. Answer me this, then rest, young champion. Would you consider a dictionary for a companion? ")
    d = {input_one: input_two, input_three: input_four, input_five: input_six, input_seven: input_eight}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(poem_responses()) 
 #   {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower().strip() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")
