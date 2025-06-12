# Correct Email and Password Game

email = input("Apna Email Bata : ")


if '@'  in email:
    passwd = input("Apna Passowrd Bata")
    if email == "ratnesh134@gmail.com" and passwd == '1234':
        print("Welcome Home")

    elif email == "ratnesh134@gmail.com" and passwd != '1234':
        print("Your Password is wrong")
        passwd = input("Phir se password bata : ")

        if passwd == "1234":
            print("Finally correct")
        else :
            print("reset your password")


    else :
        print("Wrong Password or Email id")

else:
    print("Wrong Format of Email")

