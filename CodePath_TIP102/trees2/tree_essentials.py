###############################################################
# PHASE 1: Core 4 Traversals
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# # Inorder
# left - node - right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    

# Preorder
# node - left - right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left) # but better use 1 list so no mutation
        res += self.preorderTraversal(root.right)
        return res
    


# Postorder
# left - right - node
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
    

# Level Order Traversal <- BFS
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node: # to avoind appending null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # so q doesnt add null nodes to result
                res.append(level)
        return res
    

###############################################################
# PHASE 2: Depth, Height, Count — Bottom-Up Patterns
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Max Depth of a tree
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Count nodes
def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + countNodes(root.left), countNodes(root.right)


# Sum of Left Leaves
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    total += self.sumOfLeftLeaves(root.left)
    total += self.sumOfLeftLeaves(root.right)
    return total