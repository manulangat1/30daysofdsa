"""
Also known as sinking sort.
"""


def bubleSort(nums):
    # pass
    """
    time complexity is o (n2)
    space complexity is 0(1)
    only use when space is a concern and input is already sorted.
    """
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if nums[k] < nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
    return nums


print(bubleSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8]))
