"""
    find the min and max elem in unsorted array and putting them in correct position in sorted array 
    time complexity is O (n2)
    space complexity is O (1)
"""


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selectionSort([10, 90, 30, 40, 70, 20, 100, 1, 3, 4, 5, 7]))
