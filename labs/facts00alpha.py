#!/usr/bin/python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random
def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value associated with text"
    for catfact in r.json()["all"]:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found

def random_fact():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    fact_list=[]
    for x in r.json()["all"]:
        fact_list.append(x.get("text"))
    print("\nEnjoy a random cat fact!")
    print("***************************")
    print(random.choice(fact_list))
    
#main()
random_fact()

def most_upvotes():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    print(max
most_upvotes()
