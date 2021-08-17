import random

random_number = random.randint(1,10)    #numbers 1-10

i = 0               #switch

while i == 0:
    userI = input("Guess a number between 1 and 10: ")
    userI = int(userI)
    if userI == random_number:
        print("You guessed correct!\n")
        print("Do you want to keep playing? (y/n)")
        userYN = input()
        if(userYN == "y"):
            i = 0
        else:
            break
    elif userI < random_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

