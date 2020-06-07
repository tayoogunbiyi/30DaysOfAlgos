def single_number_1(arr):
    ht = {}
    for v in arr:
        ht[v] = ht.get(v, 0) + 1

    for key in ht:
        if ht[key] == 1:
            return key


def single_number_2(arr):
    arr.sort()
    for i in range(len(arr)):
        left = arr[i-1] if i-1 >= 0 else None
        right = arr[i+1] if i+1 < len(arr) else None
        if arr[i] != left and arr[i] != right:
            return arr[i]


def single_number_3(arr):
    single_num = 0
    for num in arr:
        single_num ^= num
    return single_num
