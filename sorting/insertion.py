"""
take first element from unsorted array and find its correct position in sorted array
"""


def insertionSort(nums):
    """
    time complexity is O(n2)
    space complexity is O (1)

    use it when we have insufficient memory.
    use when dealing with continuous inflow of numbers.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertionSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8]))
