#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"): #missing a colon
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input() #changed input from deprecated version
    if calc1.lower == "q": #set case to lower on q and set lower method
        break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input() #changed input from deprecated version
    if calc2.lower == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input() #changed input from deprecated version
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2)) #added quotations to new line
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
