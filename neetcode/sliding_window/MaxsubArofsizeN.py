'''
Given nums = [-1, 2, 3, 4, 1] and k=2
find the max sum of subarray
'''

def maxSubarr(nums, k):
    max_sum = 0
    l = 0
    cur_sum = 0
    for r in range(1, len(nums)):
        while k:
            cur_sum += nums[r]
        max_sum = max(max_sum, cur_sum)
        
    return max_sum

print(maxSubarr([-1, 2, 3, 4, 1], 3))



