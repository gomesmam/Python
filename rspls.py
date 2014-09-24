# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # convert name to number 
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "invalid name"
    
    return number



def number_to_name(number):
    # convert number to a name using
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "invalid number"
    
    return name
    

    

def rpsls(player_choice): 
    # main function of the game
    
    print
    
    # player's choice
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)

    # computer's choice
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = comp_number - player_number
    print difference
    remainder = difference % 5
    print remainder 
    
    # use if/elif/else to determine winner, print winner message
    if remainder == 1:
        print "Computer wins!"
    elif remainder == 2:
        print "Computer wins!"
    elif remainder == 3:
        print "Player wins!"
    elif remainder == 4:
        print "Computer wins!"
    else:
        print "We have a tie"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
