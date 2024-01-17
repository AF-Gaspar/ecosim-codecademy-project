#This file contains utility functions for ecosim

def input_scrub_int():
    #This function keeps prompting the user to input an integer until one is entered
    while True:
            try:
                user_choice = int(input("Enter an integer> "))
                return user_choice
            except:
                 print("That's not an integer.")