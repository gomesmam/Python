# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

range = 100
allowed_guess = 7
number_guesses = 0


# helper function to start and restart the game
def new_game(range):
    # initialize global variables used in your code here
    global secret_number, allowed_guess
    secret_number = random.randrange(0, range)   
    print "New Game. Range is from 0 to", range
    print "Number of remaining guesses is:", allowed_guess
    print
    print



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range, allowed_guess
    allowed_guess = 7
    range = 100
    new_game(range)
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range, allowed_guess
    allowed_guess = 10
    range = 1000
    new_game(range)
    
def input_guess(guess):
    # main game logic goes here	
    global allowed_guess, number_guesses 
    inputed_guess = int(guess)
    print "Guess was", inputed_guess
    if inputed_guess < secret_number:
        print "Lower"
    elif inputed_guess > secret_number:
        print "Higher"
    else:
        print "Correct"
    
    if number_guesses < allowed_guess - 1:
        number_guesses = number_guesses + 1
        print "Number of remaining guesses is:", allowed_guess - number_guesses
    else:
        print "Game over. No more guesses"
        print
        new_game(range)
    print 
    

    
# create frame
f = simplegui.create_frame("Guess the Number Game",200,200)

# register event handlers for control elements and start frame
f.add_button("Range: [0 - 100)", range100, 200)
f.add_button("Range: [0 - 1000)", range1000, 200)
f.add_input("Guess", input_guess, 200)

# call new_game 

new_game(range)


# always remember to check your completed program against the grading rubric

