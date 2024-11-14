"""
    Divide arr into 2 parts 
    take the first element from unsorted array and place it in its correct posn in sorted arr. 
    repeat until sorted arr is empty. 
    Use when there is a continuous inflow of numbers are we want to keep them sorted
"""


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertionSort([10, 90, 30, 40, 70, 20, 100, 1, 3, 4, 5, 7]))
