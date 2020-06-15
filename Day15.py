def number_of_steps(num):
    steps = 0
    while num:
        if num & 1:
            num -= 1
        else:
            num = num // 2
        steps += 1
    return steps
