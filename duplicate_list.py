lst = list(map(int,input("Enter the number using comma ").split(',')))

n_lst = []

for i in lst:
    if i not in n_lst:
        n_lst.append(i)

    else:
        continue


print("Non Duplicated list as as follows")

print(n_lst)

