def find_missing_number(nums):
    nums.sort()
    # since the numbers lie between 0 and n. The first number must be 0.
    # If the first number isn't 0, then 0 is the missing number
    if nums[0] != 0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]+1:
            return nums[i-1]+1
    
    # If at the end,there's no number that isn't equal to the number of it's left,
    # the missing number is just the last number plus 1. 
    # imagine a case like nums = [0,1,2,3,4]
    # 5 is the missing number.

    return nums[-1]+1



def find_missing_number_2(nums):
    res = 0
    n = len(nums)+1

    for i in range(0,n):
        res ^= i
        
    for n in nums:
        res ^= n
    return res

def find_missing_number_3(nums):
    arr_sum = sum(nums)
    sum_to_n = len(nums)*(len(nums)+1) / 2
    return sum_to_n-arr_sum