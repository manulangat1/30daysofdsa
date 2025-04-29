import math


def binary(nums, search):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while not (nums[mid] == search):
        if search < nums[mid]:
            right = mid - 1
        if search > nums[mid]:
            left = mid + 1
        mid = (left + right) // 2
    return mid


print(binary([1, 2, 3, 4, 5, 6, 7], 3))
