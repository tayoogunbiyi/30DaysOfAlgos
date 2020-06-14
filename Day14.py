def shuffle(nums, n):
    i = 0
    j = n
    res = []
    for k in range(n):
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j += 1
    return res
