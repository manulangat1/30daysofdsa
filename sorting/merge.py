"""
Is  a divide and conquer algorithm.
Divide into halves and keep halving until they became too small to be broken further.
merge halves by sorting them.
"""


def merge(nums, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = nums[i]
    for j in range(0, n2):
        R[j] = nums[j]
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        nums[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = R[j]
        j += 1
        k += 1


def mergeSort(nums, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(nums, l, m)
        mergeSort(nums, m + 1, r)
        merge(nums, l, m, r)
    return nums


print(mergeSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8], 0, 9))
