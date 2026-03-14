# Fibonacci Series Printing

n = int(input("Enter the number of terms to print : "))

def fib(n):

    # Base Condition
    if n==1 or n==2:
        return 1
    
    else:

        return fib(n-1) + fib(n-2)
        


for i in range(1, n+1):
    print(fib(i), end=" ")

print("\n")