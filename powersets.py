def subsets(nums):

    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            return res.append(subset.copy())

            

        # Decision to include num[i]

        subset.append(nums[i])
        dfs(i+1)

        # Decision not to incluse num[i]

        subset.pop()
        dfs(i+1)

    dfs(0)

    return res


lst = list(map(int , input("Enter the list of number : ").split()))

print(subsets(lst))

