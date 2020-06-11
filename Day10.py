def pivotIndex(nums):
    right_sum = sum(nums)
    left_sum = 0 # this variable computes the sum to the left on the fly.

    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
