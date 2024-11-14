"""
    - aka sinking sort
    - repeatedly compare each pair of adjacent items and swap them if they are in the wrong order
    - Time complexity is O(n)2
    - use when space is a concern since space complexity is O(1)
    - avoid when time is an issue. 
"""


def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubbleSort([10, 90, 30, 40, 70, 20, 100, 1, 3, 4, 5, 7]))
