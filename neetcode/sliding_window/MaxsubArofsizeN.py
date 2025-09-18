'''
Given nums = [-1, 2, 3, 4, 1] and k=2
find the max sum of subarray
'''

def maxSubarrSum(nums, k):
    max_sum = float('-inf')
    l = 0
    cur_sum = 0
    for r in range(len(nums)):
        cur_sum += nums[r]
        if (r - l + 1) > k:
            cur_sum -= nums[l]
            l+=1
        
        if (r - l + 1) == k:
            max_sum = max(max_sum, cur_sum)
    return max_sum


print(maxSubarrSum([-1, 2, 3, 4, 1], 3))



