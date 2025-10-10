'''
Trapping Rain Water
Solved 
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
'''


def trap(height):
    # [0,2,0,3,1,0,1,3,2,1]
    res = 0
    n = len(height)
    maxLeft = len(height) * [0]
    maxRight = len(height) * [0]
    maxLeft[0] = height[0]
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i-1], height[i])
    
    maxRight[n - 1] = height[n - 1]
    for i in range(n-2, -1, -1):
        maxRight[i] = max(maxRight[i+1], height[i])

    for i in range(n):
        res += min(maxRight[i], maxLeft[i]) - height[i]
    return res
print(trap([0,2,0,3,1,0,1,3,2,1]))


class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        if not height:
            return 0

        n = len(height)-1
        l,r = 0, len(height)-1
        res = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
        

