'''

Binary Tree Maximum Path Sum
Solved 
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:



Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.


      -10
      /  \
     9   20
         / \
        15  7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_max = dfs(left_max.left)
            right_max = dfs(right_max.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
             # Update global ans
            max_sum = max(max_sum, node.val + left_max + right_max)
            # return best-one way path to parent
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return max_sum
    
    # Time: O(n)
    # Space: O(h)