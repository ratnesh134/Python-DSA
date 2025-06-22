def multiply(a=1,b=1):
    '''
    Here we are multiplying two numbers 
    without using the product keyword instead 
    we are using recursive function to do it
    '''

    if b == 1:  # Base Case
        return a

    else:
        return a+ multiply(a,b-1)


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

res = multiply(a,b)

print(res)
