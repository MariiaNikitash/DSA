'''
Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Plan: convert nums to a set to eliminate dubes
have a maxLen var to track the longest sequence

iterate over each num in a set of nums
check if the num - 1 is not in the set then assign length var to 1 and enter a loop to check while n + 1 in a set we increebt our leng then tke max of the len and max and return in

!!!! DO NOT FORGET ABOUT MOVING NUM IN WHILE LOOP so either num+=1 or while num+length
'''
def LongestConsequtiveSeq(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    maxLen = 0
    setNums = set(nums)
    for num in setNums:
        if (num-1) not in setNums:
            cur_len = 1
            while (num+cur_len) in setNums:
                cur_len +=1
            maxLen = max(maxLen, cur_len)
    return maxLen

print(LongestConsequtiveSeq([2,20,4,10,3,4,5]))
print(LongestConsequtiveSeq([2]))

