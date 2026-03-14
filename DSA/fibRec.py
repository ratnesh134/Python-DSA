# Fibbonacci Series by Recursion

n = int(input("Enter the nth term of fibonnaci series : "))

def fib(n):

    # Base Condition
    if n == 1 or n == 2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
    

print(fib(n))