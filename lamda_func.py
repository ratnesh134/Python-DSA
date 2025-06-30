lst = list(map(int, input("Enter a list of number : ").split(" ")))


def sum_result(func,lst):
    result = 0
    for i in lst:
        if func(i):
            result = result + i

    return result

sum_even = lambda x : x%2==0
odd_sum = lambda x: x%2 != 0
div_sum = lambda x: x%3 == 0

print(sum_result(sum_even,lst))
print(sum_result(odd_sum,lst))
print(sum_result(div_sum,lst))
