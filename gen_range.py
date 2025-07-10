# Implementing range function using generator


def mera_range(start,end):

    for i in range(start,end):

        yield i

for i in  mera_range(15,26):
    print(i)


