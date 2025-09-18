'''
Maximum Subarray
Solved 
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Time N, Space 1
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
    
        return max_sum