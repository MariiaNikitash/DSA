class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        U: return a min value in rotated sorted array using bin search (log n)
        P: implement bin search by creating l, r pointers:
        firstly check if l smaller then right, meaning array is sorted then we can stop loop and return l
        else: we compute the middle pointer and check if it is a part of sorted left or right part of arr
        if the mid value greater than left, it means smallest val is in the right part, e update left then we see that the array is 
        sorted, so return tracked res = min(res, nums[m]) during loop
        '''

        l,r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m 
        return res