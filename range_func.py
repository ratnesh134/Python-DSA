# Creating our own range function and understanding iterators and iterables


class my_range:

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):

        return my_range_iterator(self)


class my_range_iterator:

    def __init__(self,iterable_object):

        self.iterable = iterable_object

    def __iter__(self):
        return self

    def __next__(self):

        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start
        self.iterable.start += 1
        return current

for i in my_range(1,11):
    print(i)

