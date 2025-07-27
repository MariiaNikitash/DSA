# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
we are covering 3 cases when we have only 1 child left or right or if we have both nodes
'''
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else: # we are on node to delete
            # if one of leaves dont exist just update
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # if 2 childs exists find min from right subtree
            # find inorder successor (leftmost in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root