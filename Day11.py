def reverseOnlyLetters(S):
    arr = [ch for ch in S]
    l = 0
    r = len(arr)-1
    while l <= r:
        if not arr[l].isalpha():
            l += 1
        elif not arr[r].isalpha():
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    # print(arr)
    return ''.join(arr)
