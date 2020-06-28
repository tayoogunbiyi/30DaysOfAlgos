def double_step(n):
    if n <= 1:
        return 1
    return double_step(n-1) + double_step(n-2)
    


def double_step_2(n):
    if n == 0 or n == 1:
        return 1

    first = 1
    second = 1
    
    for i in range(2,n+1):
        old_second = second
        second = first
        first = first + old_second
    return first

for i in range(1,45):
    print('ans --->',double_step_2(i))
