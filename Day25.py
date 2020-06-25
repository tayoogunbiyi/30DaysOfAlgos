def add_to_array(arr,k):
    j = len(arr)-1
    carry = k
    while j >= 0:
        total = arr[j] + carry
        arr[j] = total % 10
        carry = total // 10
        if total < 10:
            break
        j-=1
    
    if carry:
        return [1] + arr
    return arr
print(add_to_array([1,9,9],1))
print(add_to_array([9,9,9],1))
print(add_to_array([1,2,3],6))
print(add_to_array([1,2,3],9))
print(add_to_array([9],1))
print(add_to_array([1],9))
print(add_to_array([1,0],9))




            