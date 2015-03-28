import random

def getGuess():
    while True:
        try: 
            return int(raw_input("Guess:"))
        except :
            print "Not a valid value"
        

random.seed()
number = random.randrange(0, 50, 1)

print number

guesscount = 0

while True:
    guess = getGuess()
    guesscount += 1
    if guess == number:
        print "Correct, " + str(guesscount) + " guesses"
        quit()
    elif guess > number:
        print "Too high!"
    else:
        print "Too low!"
      
