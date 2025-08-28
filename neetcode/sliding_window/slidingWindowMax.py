from typing import List
# Brute Force 
# Time O(n * (k-1))
# Space O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        given array I need to slide the window of size k and
        to res add max element of window
        '''
        res = []
        
        for r in range(len(nums) - k + 1):
            window = nums[r:r+k]
            
            res.append(max(window))
        return res