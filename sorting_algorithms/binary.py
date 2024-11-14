"""
    Faster than linear search. 
    Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one 
    Works only for sorted arrays

    Time complexity 
        worst O(log n )
        best O(1)
"""

import math


def binarySearch(arr, item):
    left = 0
    right = len(arr) - 1
    mid = math.floor((left + right) / 2)

    while not (arr[mid] == item):

        if item < arr[mid]:
            right = mid - 1
        if item > arr[mid]:
            left = mid + 1

        mid = math.floor((left + right) / 2)
    return mid


print(binarySearch([1, 2, 3, 4, 5, 6, 7], 3))
