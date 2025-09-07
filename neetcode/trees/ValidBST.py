'''
Valid Binary Search Tree
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.



Plan:
Use rectusion and track thje boundaries when I do recursion on left side set biggest val as a root, fpr thr right set root val as the smallest
Time O(n), Space O(n)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_boundary, right_boundary):
            if not node:
                return True
            if not (left_boundary < node.val and node.val < right_boundary):
                return False
            return dfs(node.left, left_boundary, node.val) and dfs(node.right, node.val, right_boundary)

        return dfs(root, float('-inf'), float('inf'))