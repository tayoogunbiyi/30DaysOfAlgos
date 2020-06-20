# Approach 1
def range_sum(arr, i, j):
    sum_ = 0
    for k in range(i, j+1):
        sum_ += arr[k]
    return sum_

# Approach 2 - When range_sum is called repeatedly on the same array


class RangeSumArray():
    def __init__(self, arr):
        self.prefix_sum_cache = [0 for _ in range(len(arr)+1)]

        for i in range(len(arr)):
            self.prefix_sum_cache[i+1] = self.prefix_sum_cache[i] + arr[i]

    def range_sum(self, i, j):
        return self.prefix_sum_cache[j+1] - self.prefix_sum_cache[i]
