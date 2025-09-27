
def factorial(num):

    if num == 1:
        return 1

    else:

        num = num * factorial(num-1)
        return num

result = factorial(5)

print(result)
