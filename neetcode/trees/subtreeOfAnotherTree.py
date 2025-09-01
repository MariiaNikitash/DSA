'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the
 same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.


'''
# Time: O(M * N) for potentially visiting evry node in both trees
# Space: O(m + n) recursion stack

class Solution:   
    # apply same tree func recursively on root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

# check if tre and subtree are same recursively by comparing the vals
    def sameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            return  (self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right))
        return False
