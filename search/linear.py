"""
Items are searched one by one.
- Also known as sequential search.
"""


def linear(nums, item):
    for i in nums:
        if i == item:
            return True
    return False


print(linear([2, 10, 3, 7, 1, 4, 6, 5, 9, 8], 10))
