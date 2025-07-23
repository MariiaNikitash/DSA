class Solution:
    def search(self, nums, target):
        '''Given the rotated sorted array nums and an integer target,
        return the index of target within nums, or -1 if it is not present. Do in Log N time'''
        l,r = 0, len(nums) -1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
    # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
    # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1