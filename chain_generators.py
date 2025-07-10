# Chaining the fibonacci series and sqaure function using generators


def fib_num(nums):

    x,y = 0,1

    for _ in range(nums):
        x, y = y, x+y
        yield x


def square(nums):

    for num in nums:

        yield num**2


print(sum(square(fib_num(10))))
