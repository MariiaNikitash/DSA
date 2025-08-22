'''
3Sum
Solved 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
'''

# Brute Force
class Solution:
    def threeSum(nums):
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        return [list(i) for i in res]
    

# Two pointer optimized solution
'''
sort the array so we know if valye already appeard 
Outer loop for the first value
inner loop to get 2 otehr vlues by using left and right pointetr
shift pointers in nums[i] + nums[r] + nums[l] == 0 add to result and update pointers and do it till w find all pairs 
'''
def ThreeSum(nums):
    nums.sort()
    res = [] 
    n = len(nums)
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue # skip dublicate

        if nums[i] > 0: # if first val > 0 everything else will be larger and not gonna == 0
            break 
        l,r = i+1, n-1
        while l < r:
            curSum = nums[i] + nums[l] + nums[r]
            if curSum == 0:
                res.append([nums[i],  nums[l], nums[r]])
                l +=1
                r -=1
                while l < r and nums[l] == nums[l-1]:
                    l +=1
                while l < r and nums[r] == nums[r+1]:
                    r -=1
            elif curSum > 0:
                r -=1
            else:
                l +=1
    return res

print(ThreeSum([-1,0,1,2,-1,-4]))
print(ThreeSum([-1, 1,1]))

# Time O n log n + (n^2)  === (n^2)
# space: O(1)