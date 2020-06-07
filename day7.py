def reverse_arr(arr):
    reversed_arr = []
    j = len(arr)-1
    while j >= 0:
        reversed_arr.append(arr[j])
        j -= 1

    return reversed_arr


def reverse_arr_inplace(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
