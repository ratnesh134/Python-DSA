def square(num):

    for i in range(1,num+1):
        yield i**2


gen = square(20)

print(next(gen))
print(next(gen))
print(next(gen))
