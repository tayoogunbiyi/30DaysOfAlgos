
# slow solution
def find_length_of_smallest_subarray_gt_k(arr, k):
    ans = len(arr)+1

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            curr_subarray_sum = sum(arr[i:j+1])
            if curr_subarray_sum > k:
                ans = min(ans, j-i+1)
    return ans if ans != len(arr)+1 else 0


def find_length_of_smallest_subarray_gt_k_2(arr, k):
    i = 0
    j = 0
    curr_window_sum = 0
    ans = len(arr)+1
    while j < len(arr):
        curr_window_sum += arr[j]
        while i < len(arr) and curr_window_sum > k:
            ans = min(ans, j-i+1)
            curr_window_sum -= arr[i]
            i += 1
        j += 1
    return ans if ans != len(arr)+1 else 0


print(find_length_of_smallest_subarray_gt_k([1, 2, 3, 4, 5, 6, 7, 8], 20))
print(find_length_of_smallest_subarray_gt_k([1, 2, 3, 4, 5, 6, 7, 8], 7))

print(find_length_of_smallest_subarray_gt_k_2([1, 2, 3, 4, 5, 6, 7, 8], 20))
print(find_length_of_smallest_subarray_gt_k_2([1, 2, 3, 4, 5, 6, 7, 8], 7))
print(find_length_of_smallest_subarray_gt_k([1, 2, 3, 45, 56], 10000))
