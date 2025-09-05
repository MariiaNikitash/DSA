'''
Binary Tree Level Order Traversal
Solved 
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Time:  O(N)
Space: O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = deque([root])

        while q:
            cur_res = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_res.append(node.val)
            

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur_res)

            
        return res