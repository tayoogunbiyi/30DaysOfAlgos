def two_sum(numbers, target):
    l = 0
    r = len(numbers)-1
    while l < r:
        total = numbers[l]+numbers[r]
        if total == target:
            return True
        elif total < target:
            l += 1
        else:
            r -= 1
    return False
