# Recursion

n = int(input("Enter the number : "))

def factorial(n):

    # Base Condition
    if n == 0 or n == 1 :
        return 1
    
    else:
        return n * factorial(n-1)
    
print(f' The factorial of {n} is {factorial(n)}')