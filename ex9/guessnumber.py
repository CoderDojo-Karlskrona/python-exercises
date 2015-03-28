import random

random.seed()
number = random.randrange(0, 100, 1)

guesscount = 0

while True:
    guess = int(raw_input("Guess: "))
    guesscount = guesscount + 1
    if guess == number:
        print "Correct, " + str(guesscount) + " guesses"
        break
    elif guess > number:
        print "Too high!"
    else:
        print "Too low!"
      
