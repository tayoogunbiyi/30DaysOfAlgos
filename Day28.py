def maxProduct(nums):
    max1 = max(nums[0],nums[1])
    max2 = min(nums[0],nums[1])        

    for n in nums[2:]:
        if n >= max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    return (max1-1)*(max2-1)