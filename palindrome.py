def palindrome(string):

    if len(string) <= 1:
        print("Palindrome")

    else:
        if string[0] == string[-1]:
            palindrome(string[1:-1])
        else:
            print("Not a Palindrome")


string = input("Enter the string : ")

palindrome(string)
