#!/usr/bin/python5
#Capstone Project for TLG Learning
#Authored by Luke Thompson
from random import randint
import dice
import sys
import time
from itertools import islice

#Would like to do: 
#Implement class document and inheritance for functios
#format print output for multiple readlines or other method to preclude "text walls" from code
#KISS but streamline code (reduce conditional statements)


print(
"""
On the High Seas
A Choose Your Own Adventure Python Script
Written by Luke Thompson
""")


#--------Introduction Function----------
def intro():
    intro = open("try.txt", "r")
    print(intro.readlines()[0])
    faction()

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
        print(factionpopout.readlines()[8]) #calls Royal Irish Navy line from text document
        time.sleep(1)
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmfaction = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmfaction.strip() == "1":
            attributestutorialn() 
        elif confirmfaction.strip() == "2":
            faction() #calls restart on faction()
        elif confirmfaction.lower().strip() == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            faction()
    elif playerfaction.strip() == "2":
        print(factionpopout.readlines()[13])
        time.sleep(1)
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmfaction = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmfaction.strip() == "1":
            attributestutorialp()
        elif confirmfaction.strip() == "2":
            faction() #calls restart on faction()
        elif confirmfaction.lower().strip() == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            faction()
    elif playerfaction.lower().strip() == "q":
        sys.exit()
    else:
        print("Please make a valid selection: 1, 2, or \'q\' for quit.")
        faction()

#----------------Blackfire Consortium Attribute Prompt----------------
def attributestutorialp():
    displayattributesp = input("Would you like to display information regarding your character's attributes and their employ in this adventure on the high seas? Use y/n > ")
    if displayattributesp.strip().lower() == "y":
        print("\n" + "*************************************************************" + "\n")
        attrpopoutp = open("try.txt", "r")
        print(attrpopoutp.readlines()[1])
        print("""
Strength is a measure of your character's phyiscal prowess, and allows your character to be more powerful in melee combat.
Dexterity is a measure of your character's agility, aerial awareness, and accuracy in ranged combat.
Constitution is your character's hardiness and fortitude, and propensity to resist or recover from ailments.
Intelligence conveys your character's knowledge base and ability to learn, reason through complex or confusing circumstances, puzzles, or riddles.
Wisdom encompases your character's common sense, awareness, and intuition.
Charisma is a representation of your character's magnetism, personality, ability to lead, and appearance.""")
        pcpirate()
    elif displayattributesp.strip().lower() == "n":
        pcpirate()
    elif displayattributesp.strip().lower() == "q":
        sys.exit()
    else:
        print("Please make a valid selection: y/n or \'q\' for quit.")
        attributestutorialp()

#---------------Blackfire Consortium Class Selection----------------
def pcpirate():    
    print(
    """
    Choose a player class, or press \'q\' to exit.
    [1]: Corsair (Brawler)
    [2]: Swashbuckler (Rogue)
    [3]: Battlemage (Mage)
    [4]: Huntsman (Ranger)
    [5]: Vindictive Bastard (Paladin)
    """)
    classpopoutp = open("try.txt", "r")
    classchoicep = input(" > ")
    if classchoicep == "1":
        print(classpopoutp.readlines()[14])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcp = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcp.strip() == "1":
            begincorsair()
        elif confirmpcp.strip() == "2":
            pcpirate()
        elif confirmpcp.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcpirate()
    elif classchoicep == "2":
        print(classpopoutp.readlines()[15])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcp = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcp.strip() == "1":
            beginswash()
        elif confirmpcp.strip() == "2":
            pcpirate()
        elif confirmpcp.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcpirate()
    elif classchoicep == "3":
        print(classpopoutp.readlines()[16])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcp = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcp.strip() == "1":
            beginbattlemage()
        elif confirmpcp.strip() == "2":
            pcpirate()
        elif confirmpcp.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcpirate()
    elif classchoicep == "4":
        print(classpopoutp.readlines()[17])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcp = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcp.strip() == "1":
            beginhuntsman()
        elif confirmpcp.strip() == "2":
            pcpirate()
        elif confirmpcp.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcpirate()
    elif classchoicep == "5":
        print(classpopoutp.readlines()[18])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcp = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcp.strip() == "1":
            beginvinbas()
        elif confirmpcp.strip() == "2":
            pcpirate()
        elif confirmpcp.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcpirate()
    elif classchoicep == "q":
        sys.exit()
    else:
        print("Please make a valid selection: 1-5, or \'q\' for quit.")
        pcpirate()

#----------------Royal Navy Attribute Prompt----------------
def attributestutorialn():
    displayattributesn = input("Would you like to display information regarding your character's attributes and their employ in this adventure on the high seas? Use y/n > ")
    if displayattributesn.strip().lower() == "y":
        print("\n" + "*************************************************************" + "\n")
        attrpopoutn = open("try.txt", "r")
        print(attrpopoutn.readlines()[1])
        print("""
Strength is a measure of your character's phyiscal prowess, and allows your character to be more powerful in melee combat.
Dexterity is a measure of your character's agility, aerial awareness, and accuracy in ranged combat.
Constitution is your character's hardiness and fortitude, and propensity to resist or recover from ailments.
Intelligence conveys your character's knowledge base and ability to learn, reason through complex or confusing circumstances, puzzles, or riddles.
Wisdom encompases your character's common sense, awareness, and intuition.
Charisma is a representation of your character's magnetism, personality, ability to lead, and appearance.""")
        pcnavy()

#----------------Royal Navy Class Selection------------------        
def pcnavy():
    print(
    """
    Choose a player class, or press \'q\' to exit.
    [1]: Marine (Brawler)
    [2]: Barrelman (Rogue)
    [3]: Shipwizard (Mage)
    [4]: Warden (Ranger)
    [5]: Justiciar (Paladin)
    """)
    classpopoutn = open("try.txt", "r")
    classchoicen = input(" > ")
    if classchoicen == "1":
        print(classpopoutn.readlines()[9])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcn = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcn.strip() == "1":
            beginmarine()
        elif confirmpcn.strip() == "2":
            pcnavy()
        elif confirmpcn.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcnavy()
    elif classchoicen == "3":
        print(classpopoutn.readlines()[11])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcn = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcn.strip() == "1":
            beginshipwiz()
        elif confirmpcn.strip() == "2":
            pcnavy()
        elif confirmpcn.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcnavy()
    elif classchoicen == "4":
        print(classpopoutn.readlines()[19])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcn = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcn.strip() == "1":
            beginwarden()
        elif confirmpcn.strip() == "2":
            pcnavy()
        elif confirmpcn.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcnavy()
    elif classchoicen == "5":
        print(classpopoutn.readlines()[12])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcn = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcn.strip() == "1":
            beginjust()
        elif confirmpcn.strip() == "2":
            pcnavy()
        elif confirmpcn.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcnavy()
    elif classchoicen == "2":
        print(classpopoutn.readlines()[10])
        print("Are you happy with this selection? Once you confirm, you cannot go back!")
        confirmpcn = input("Select [1] > to confirm or [2] > to start over > ")
        if confirmpcn.strip() == "1":
            beginbarrel()
        elif confirmpcn.strip() == "2":
            pcnavy()
        elif confirmpcn.strip().lower == "q":
            sys.exit()
        else:
            print("Please make a valid selection: 1, 2, or \'q\' for quit.")
            pcnavy()
    else:
        print("Please make a valid selection: 1-5, or \'q\' for quit.")
        pcnavy()
intro()
