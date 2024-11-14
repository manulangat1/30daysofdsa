"""
    Also known as sequetial search. 
    We move one by one while comparing the value. 
"""

"""
    Time complexity is O(n)
    space complexity is O(1)
"""


def linearSearch(arr, item):
    for i in arr:
        if i == item:
            return True
    return False


print(linearSearch([1, 2, 3, 4, 5, 6, 7], 2))
