def memo(num,d):

    '''
    Solving Fibonacci Series using Memoization
    '''
    # Base Case

    if num in d:
        return d[num]

    else:

        d[num] = memo(num-1,d) + memo(num-2,d)

        return d[num]


d = {0:1,1:1}

print(memo(48,d))

