import random
print("Guess a four digit number, \nfor each correct number guessed at the correct index you will recieve a cow, \nand for each correct number guesed at the incorrect index you will recieve a bull.")

def bovineAccuracy():
    guessing = True
    num = str(random.randint(1000, 9999))
    guesses = 0
    while guessing == True:
        cowBull = [0,0]
        guess = input("enter your guess now: ")
        guesses +=1
        if guess == "num":
            print(num)
        if guess == num:
            guessing = False
            return print("You got it! Congrats! It only took you "+str(guesses)+" guesses!")
        cowIndex = 0
        while cowIndex < len(num):
            if guess[cowIndex] == num[cowIndex]:
                cowBull[0] += 1
            cowIndex += 1
        bullIndex = 0
        while bullIndex < len(num):
            if num.__contains__(guess[bullIndex]) and guess[bullIndex] != num[bullIndex]:
                cowBull[1] += 1
            bullIndex += 1
        print("cows:"+str(cowBull[0])+" bulls:"+str(cowBull[1]))

bovineAccuracy()