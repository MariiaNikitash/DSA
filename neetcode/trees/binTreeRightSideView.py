'''
Binary Tree Right Side View
Solved 
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right
side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3]

Output: [1,3]

REMEBER to Consider right nodes on left subtree

       1
     /   \
    2     3
     \
      5
Out: [1,3,5]

Time, Space is O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == len_q - 1:
                    res.append(node.val)

        return res