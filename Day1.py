'''
Find Kth smallest (Points - 20)
Given an array of numbers, find the Kth smallest item.
This means that if k was 1, we'd find the first smallest. if k was 2, we'd find the second smallest and so on.
Your solution should be faster than O(n log n) where n is the size of the array.

'''
# heapq is python's built in heap data structure. it provides min heap functionalities by default
# However we can tweak it to make it give us max heap functionality as that's what we need in this question
# See this in solution 2
import heapq


# Solution 1
# Time Complexity - O(n log n) , space complexity - O(1) or O(log n) , depends.


def find_kth_smallest1(arr, k):
    arr.sort()
    return arr[k-1]


# Solution 2
# Time complexity - O(n log k) , space complexity - O(k)

def find_kth_smallest2(arr, k):
    # we push in -1*arr[i] so as to get the max heap functionality from a min heap
    # you know the min heap always give the minimum on removal, if we want 7 and 8 into a min heap
    #  and we instead push in -1 * 7 and -1 * 8.
    # when we want to remove, we get -8 back and this simulates having a max heap of removing the max
    # just don't forget to multiply whatever you remove from the heap by -1 again
    # to nullify the effect of the initial -1 multiplication

    heap = []
    for i in range(k):
        heapq.heappush(heap, -1*arr[i])
    i += 1
    while i < len(arr):
        heapq.heappushpop(heap, -1*arr[i])
        i += 1

    return -1*heap[0]


# Solution 3
# Time complexity - O(n) , space complexity - O(log n) [Due to space on the call stack]


def find_kth_smallest_3(arr, k):

    def partition(arr, l, r):
        pivot = (l+r)//2
        arr[r], arr[pivot] = arr[pivot], arr[r]
        insertion_idx = l
        for i in range(l, r):
            curr = arr[i]
            if curr < arr[r]:
                arr[insertion_idx], arr[i] = arr[i], arr[insertion_idx]
                insertion_idx += 1
        arr[insertion_idx], arr[r] = arr[r], arr[insertion_idx]
        return insertion_idx

    def helper(arr, l, r, target_idx):
        while r >= l:
            pi = partition(arr, l, r)
            if pi == target_idx:
                return arr[pi]
            elif pi > target_idx:
                r = pi-1
            else:
                l = pi+1
        return arr[l]
    return helper(arr, 0, len(arr)-1, k)
