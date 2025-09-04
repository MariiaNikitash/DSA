'''
Lowest Common Ancestor in Binary Search Tree
Solved 
Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q,
return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.

Example 1:



Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check if p.val is > root.val we search right
        # if q.val is < root.val we search left
        # else p and q in different subtree and this node is LCA
        cur = root
        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur

# Time: Log N, bc e search one side of tree
# Space: 1


# Now recursion
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
# Time: Log N, bc e search one side of tree
# Space: N bc of resursion stack