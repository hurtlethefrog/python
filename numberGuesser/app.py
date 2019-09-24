import random

number = 1

guessesTaken = 0

playerName = input("please enter your name: ")

print("well " + playerName + " I'm think of a number between 1 and 20.")

for guessesTaken in range(6):
    guess = input("take a guess: ")
    guess = int(guess)
    if guess > number:
        print("too high")
    if guess < number:
        print("too low")
    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print("you got it, and it only took you " + guessesTaken + " attempts.")
        break
if guess != number:
    number = str(number)
    print("nope I was thinking of the number " + number)