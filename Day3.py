def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return True


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
