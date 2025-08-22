'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
'''


def LongestContiniousSub(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        # start of new seq
        if (n-1) not in numSet:
            cur_len = 0
            while (n + cur_len) in numSet:
                cur_len += 1
                
            longest = max(longest, cur_len)
    return longest

# Time/Space: O(n)