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
    


# Optimal using DEque to store indexes 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + l+1) >= k:
                res.append(nums[q[0]])
                l +=1
            r+=1

        return res