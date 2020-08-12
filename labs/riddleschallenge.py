#!/usr/bin/var python3
import sys
import random
"""
Riddles
Author: Luke Thompson
"""

correct = 0
def main():
    print(
    """

    A Dozen Riddles
    
    """)
    faceone()

def faceone():
    answer1 = input(
    """
    Riddle one:

    I can have no color, though there may be darkness within. 
    I have no weight and hold nothing, and if placed in a container it becomes lighter.

    a: space
    b: time
    c: air
    d: a hole
    
    """)
    if answer1.strip().lower() == "d":
        global correct 
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facetwo()
    if answer1.lower().strip() == "q":
        sys.exit()
    if answer1.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceone()
    else:
        print("The answer was: a hole")
        facetwo()

def facetwo():
    answer2 = input(
    """
    Riddle two:

    Of all your possessions, I am the hardest to guard. 
    If you have me, you will want to share me. 
    If you share me, you no longer have me.

    a: my money
    b: my time
    c: a secret
    d: my knowledge
    
    """)
    if answer2.strip().lower() == "c":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facethree()
    elif answer2.lower().strip() == "q":
        sys.exit()
    elif answer2.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facetwo()
    else:
        print("The answer was: a secret")
        facethree()

def facethree():
    answer3 = input(
    """
    Riddle three:

    Alive as you but without breath. 
    As cold in my life as in my death.
    Never a thirst, though I always drink.
    Dressed in a mail, yet never a clink.

    a: ice
    b: a fish
    c: hatred
    d: a river
    
    """)
    if answer3.strip().lower() == "b":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facefour()
    elif answer3.lower().strip() == "q":
        sys.exit()
    elif answer3.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facethree()
    else:
        print("The answer was: a fish")
        facefour()


def facefour():
    answer4 = input(
    """
    Riddle four:

    I am free for the taking through all of your life, 
    though given but once at birth. 
    I am less than nothing in weight, 
    but will fell the strongest of you if held.

    a: a life
    b: truths
    c: success
    d: breath
    
    """)
    if answer4.strip().lower() == "d":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facefive()
    elif answer4.lower().strip() == "q":
        sys.exit()
    elif answer4.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facefour()
    else:
        print("The answer was: breath")
        facefive()

def facefive():
    answer5 = input(
    """
    Riddle five:

    I have holes throughout, 
    from back to front and top to bottom to core. 
    More nothing than something within, 
    and yet I still hold water.

    a: clouds
    b: a sponge
    c: cells
    d: the ground
    
    """)
    if answer5.strip().lower() == "b":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facesix()
    elif answer5.lower().strip() == "q":
        sys.exit()
    elif answer5.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facefive()
    else:
        print("The answer was: a sponge")
        facesix()


def facesix():
    answer6 = input(
    """
    Riddle six:

    They flow and leap, but only as you pass. 
    Dress yourself in darkest black, 
    and they are darker still. 
    Always they flee in the light, 
    though without the sun there would be none.

    a: monsters
    b: lies
    c: shadows
    d: thoughts
    
    """)
    if answer6.strip().lower() == "c":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        faceseven()
    elif answer6.lower().strip() == "q":
        sys.exit()
    elif answer6.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facesix()
    else:
        print("The answer was: shadows")
        faceseven()

def faceseven():
    answer7 = input(
    """
    Riddle seven:

    They come to witness the night without being called, 
    a sailor's guide and a poet's tears. 
    They are lost to sight each day without the hand of a thief.

    a: whispers
    b: ghosts
    c: stars
    d: eyes
    
    """)
    if answer7.strip().lower() == "c":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        faceeight()
    elif answer7.lower().strip() == "q":
        sys.exit()
    elif answer7.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceseven()
    else:
        print("The answer was: stars")
        faceeight()


def faceeight():
    answer8 = input(
    """
    Riddle eight:

    The more that there is, 
    the less that you see. 
    Squint all you wish 
    when surrounded by me.

    a: darkness
    b: the sun
    c: ale
    d: nonsense
    
    """)
    if answer8.strip().lower() == "a":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facenine()
    elif answer8.lower().strip() == "q":
        sys.exit()
    elif answer8.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceeight()
    else:
        print("The answer was: darkness")
        facenine()


def facenine():
    answer9 = input(
    """
    Riddle nine:

    The life I lead is mere hours or less, 
    I serve all my time by being consumed. 
    I am quickest when thin, slowest when fat, 
    and wind is the bane of the gift that I bring.

    a: speech
    b: a cloud
    c: smoke
    d: a candle
    
    """)
    if answer9.strip().lower() == "d":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        faceten()
    elif answer9.lower().strip() == "q":
        sys.exit()
    elif answer9.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceeight()
    else:
        print("The answer was: a candle")
        faceten()

        
def faceten():
    answer10 = input(
    """
    Riddle ten:

    The man who invented it, doesn't want it for himself. 
    The man who bought it, doesn't need it for himself. 
    The man who needs it, doesn't know when he needs it.

    a: sobriety
    b: a coffin
    c: sanctuary
    d: judgement
    
    """)
    if answer10.strip().lower() == "b":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        faceeleven()
    elif answer10.lower().strip() == "q":
        sys.exit()
    elif answer10.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceten()
    else:
        print("The answer was: a coffin")
        faceeleven()

        
def faceeleven():
    answer11 = input(
    """
    Riddle eleven:

    A spirited jig it dances bright, 
    banishing all but darkest night. 
    Give it food and it will live, 
    give it water and it will die.

    a: a torchbug
    b: an optimist
    c: fire
    d: sound
    
    """)
    if answer11.strip().lower() == "c":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        facetwelve()
    elif answer11.lower().strip() == "q":
        sys.exit()
    elif answer11.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        faceeleven()
    else:
        print("The answer was: fire")
        facetwelve()


def facetwelve():
    answer12 = input(
    """
    Riddle twelve:

    Lighter than what I am made of, 
    more of me is hidden than is seen, 
    I am the bane of the mariner, 
    a tooth within the sea. Speak my name.

    a: the shore
    b: sharks
    c: booty
    d: ice
    
    """)
    if answer12.strip().lower() == "d":
        global correct
        correct += 1
        print("Correct!")
        print(f"Total number of correct answers: {correct}")
        bonus()
    elif answer12.lower().strip() == "q":
        sys.exit()
    elif answer12.lower().strip() not in ("a", "b", "c", "d"):
        print("Please make a valid selection.")
        facetwelve()
    else:
        print(f"Total number of correct answers: {correct}")
        bonus()

def bonus():
    bonusornah = input(
    """
    Bonus round?

    Double or nothing... but be warned, the final riddle is a doozy!

    y: I'm feeling lucky... let's do it!
    n: No thanks!
    
    """)
    if bonusornah.strip().lower() == "y":
        bonusriddle()
    elif bonusornah.lower().strip() == "q":
        sys.exit()
    elif bonusornah.lower().strip() not in ("y", "n"):
        print("Please make a valid selection.")
        bonus()
    elif bonusornah.lower().strip() == "n":
        print("Thanks for playing!")
        tally()
        sys.exit()

def bonusriddle():
    global correct
    bonusanswer = input(
    """
    Excellent! A princess is as old as the prince will be when the princess is 
    twice as old as the prince was when the princess' age was half the sum of 
    the present age. Which of the following, then, could be true?

    a: the prince is 20 and the princess is 30.
    b: the prince is 40 and the princess is 30.
    c: the prince is 30 and the princess is 40.
    d: the prince is 30 and the princess is 20.
    e: they are both the same age.
    f: I surely don't know!
    """
    )
    if bonusanswer.strip().lower() == ("a", "b", "d", "e", "f"):
        print("Wah wah wah wahhhhhhhh... too bad, so sad, thanks for playing!")
    elif bonusanswer.lower().strip() == "q":
        print("See ya!")
        sys.exit()
    elif bonusanswer.lower().strip() not in ("a", "b", "c", "d", "e", "f"):
        print("Please make a valid selection.")
        bonusriddle()
    elif bonusanswer.lower().strip() == "c":
        correct *= random.randint(2, 32) 
        print("Well, alrighty then, wiseacre! Getcha some points!")
        print(f"Your total score: {correct} out of 12!")
        sys.exit()

def tally():
    global correct
    if correct == 12:
        print(f"Fantastic job! You got a perfect score, 12 out of {correct}!")
    elif correct in range(9, 12):
        print(f"Very well done! You got {correct} out of 12 correct!")
    elif correct in range(6, 8):
        print(f"Not too shabby. You got {correct} out of 12 correct!")
    elif correct in range(3, 5):
        print(f"Well, then! Always room for improvement!  You got {correct} out of 12 correct.")
    elif correct in range(0, 2):
        print(f"Play again! You got {correct} out of 12 correct.")

main()
