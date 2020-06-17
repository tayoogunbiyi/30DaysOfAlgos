def reverse(x):
    rev = 0
    while x:
        rev = rev*10 + x%10
        x = x // 10
    return rev


print(reverse(102))
print(reverse(100))