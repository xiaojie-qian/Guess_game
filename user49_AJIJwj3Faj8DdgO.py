# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "\n"
    print "New game, range is 0 to 100"
    print "Number of remaining guesses is 7"
    print "\n"
    global secret_number
    global n
    n = int(math.ceil(math.log(101,2)))
    # button that changes the range to [0,100) and starts a new game 
    secret_number = random.randint(0,100)
    # remove this when you add your code    
    input_guess

# define event handlers for control panel
def range100():
    new_game()


def range1000():
    global secret_number
    global n 
    n = int(math.ceil(math.log(1001,2)))
    # button that changes the range to [0,1000) and starts a new game     
    print "New game, range is from 0 to 1000"
    print "Number of remaining guesses is 10" + "\n"
    secret_number = random.randint(0,1000)
    input_guess

def input_guess(guess):
    print "guess was " + str(guess)
    guess = int(guess)
    global n
    if n > 0:
        n= n-1
        print "Number of remaining guesses is " + str(n)
        if guess > secret_number:
            print "Lower!"+"\n"
        elif guess < secret_number:
            print "Higher!"+"\n"
        else:
            print "Correct!"+"\n"
    else: 
        print "Out of guesses"
        new_game()

# create frame
f = simplegui.create_frame("guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
f.start