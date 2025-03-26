"""
- Is a divide and conquer algorithm.
- Find pivot numbers and ensure  smaller numbers are left of the pivot and bigger numbers at right of pivot.
- extra space is not required.
- time complexity isO log N
space complexity is O(N)
"""


def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quickSort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quickSort(nums, low, pi - 1)
        quickSort(nums, pi + 1, high)

    return nums


print(quickSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8], 0, 9))
