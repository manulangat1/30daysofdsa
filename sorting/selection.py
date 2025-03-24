"""
Find min and max elem in an array and moving them to their correct posns.

"""


def selectionSort(nums):
    """
    time complexity is O(n2)
    space complexity is O (1)

    use it when we have insufficient memory.
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selectionSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8]))
