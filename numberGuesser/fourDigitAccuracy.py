import random
print("Guess a four digit number, for each correct number guessed at the correct index you will recieve a cow, and for each correct number guesed at the incorrect index you will recieve a bull.")

def bovineAccuracy():
    num = str(random.randint(1000, 9999))
    print(num)
    cowBull = [0,0]
    guess = input("enter your guess now: ")
    if guess == num:
        return print("You got it! Congrats!")
    index = 0
    while index < len(num):
        if guess[index] == num[index]:
            cowBull[0] += 1
        index += 1   
    print("cows:"+str(cowBull[0])+" bulls:"+str(cowBull[1]))

bovineAccuracy()