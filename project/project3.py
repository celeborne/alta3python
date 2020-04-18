#!/usr/bin/python5
#Capstone Project for TLG Learning
#Authored by Luke Thompson
from random import randint
import dice
import sys
import time

print(
"""
On the High Seas
A Choose Your Own Adventure Python Script
Written by Luke Thompson
""")

#--------Player Class Function-----------
def playerclass():
    classpopout = open("try.txt", "r")
    print(
    """
    Choose a player class, or press \'q\' to exit.
    [1]: Brawler
    [2]: Rogue
    [3]: Mage
    [4]: Ranger
    [5]: Paladin
    """)
    playerclass = input(" > ")

#--------Introduction Function----------
def intro():
    intro = open("try.txt", "r")
    print(intro.readlines()[0])
intro()

def faction():
    factionpopout = open("try.txt", "r")
    print(
    """
    Choose a faction to view, or press \'q\' to exit.
    [1]: Royal Irish Navy
    [2]: Blackfire Consortium
    """)
    playerfaction = input(" > ")
    if playerfaction.strip() == "1":
        print(factionpopout.readlines()[1])
        time.sleep(1)
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmfaction = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmfaction.strip() == "1":
            playerclass() 
        elif confirmfaction.strip() == "2":
            faction() #calls restart on faction
        elif confirmfaction.lower().strip() == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
    elif playerfaction.strip() == "2":
        print(factionpopout.readlines()[6])
        time.sleep(1)
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmfaction = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmfaction.strip() == "1":
            playerclass() #calls playerclass function to set player class
        elif confirmfaction.strip() == "2":
            faction() #calls restart on faction() function
        elif confirmfaction.lower().strip() == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
    elif playerfaction.lower().strip() == "q":
        sys.exit()
    else:
        print("Please make a valid selection: 1, 2, or \'q\' for quit.")
faction()

def playerclass():
    classpopout = open("try.txt", "r")
    print(
    """
    Choose a player class, or press \'q\' to exit.
    [1]: Brawler
    [2]: Rogue
    [3]: Mage
    [4]: Ranger
    [5]: Paladin
    """)
    playerclass = input(" > ")
