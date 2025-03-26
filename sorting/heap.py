"""
Uses binary heap tree.
- Insert data to binary heap tree.
- extract data from binary heap tree.
- best suited with an array.
- space complexity is O(1)
- time complexity is O(N log N )
"""


def heapify(nums, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and nums[l] < nums[smallest]:
        smallest = l
    if r > n and nums[r] < nums[smallest]:
        smallest = r

    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        heapify(nums, n, smallest)


def heapSort(nums):
    n = len(nums)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


print(heapSort([2, 10, 3, 7, 1, 4, 6, 5, 9, 8]))
