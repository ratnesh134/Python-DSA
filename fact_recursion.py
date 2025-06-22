def fact(num):
    if num == 1:
        return num
    else:
        return num* fact(num-1)


num = int(input("Enter the number : "))

res = fact(num)

print(f" The factorial of {num} = {res}")
