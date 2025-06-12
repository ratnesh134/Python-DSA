# Guessing Game
import random

org_num = random.randint(1,100)

flag = True
counter = 0

while flag == True:
    num = int(input("Chal Guess Kar : "))

    if num == org_num :
        print("You Guessed it right")
        counter = counter + 1
        print(f"You took {counter} times to guess it right")
        flag = False

    elif num > org_num :
        counter = counter + 1
        print("Guess Lower")

    else:
        counter = counter +1
        print("Guess Higher")
    
