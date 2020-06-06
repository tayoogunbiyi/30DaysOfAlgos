def dutch_national_flag_naive(nums):
    nums.sort()


def dutch_national_flag_better(nums):
    zeros_arr = []
    ones_arr = []
    twos_arr = []

    for n in nums:
        if n == 0:
            zeros_arr.append(n)
        elif n == 1:
            ones_arr.append(n)
        else:
            twos_arr.append(n)

    return zeros_arr+ones_arr+twos_arr


def dutch_national_flag_improved(nums):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        j += 1

    k = len(nums)-1
    l = k

    while k >= i:
        if nums[k] == 2:
            nums[k], nums[l] = nums[l], nums[k]
            l -= 1
        k -= 1
