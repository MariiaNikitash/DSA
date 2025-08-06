from typing import Optional
###############################################################
# PHASE 1: Core 4 Traversals
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# # Inorder
# left - node - right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


# Min Depth 
def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    # # if one of the children is None, we must go down the other
    if not root.left:
        return 1 + self.minDepth(root.right)
    if not root.right:
        return 1 + self.minDepth(root.left)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Avarage of levels in BT
def averageOfLevels(root):
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_sum = 0

        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        avg = level_sum / level_size
        res.append(avg)

    return res


###############################################################
# PHASE 3: Boolean Return – Path Logic
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Path Sum 
# tree has a path equal to target
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum  == root.val 
    #recursively substract nodes val from target sum
    remainingSum = targetSum - root.val
    return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)


# Path Sum iteratively 
def hasPathSum(root, targetSum):
    if not root:
        return False

    stack = [(root, targetSum - root.val)]  # (node, remainingSum)

    while stack:
        node, currSum = stack.pop()

        # If it's a leaf, check if the path sum matches
        if not node.left and not node.right and currSum == 0:
            return True

        # Push children with updated remaining sum
        if node.right:
            stack.append((node.right, currSum - node.right.val))
        if node.left:
            stack.append((node.left, currSum - node.left.val))

    return False


# Is summetric Tree
#        3
#     / | \ 
#    2  |  2
#   / \ | / \ 
#  7   9 9   7
# left and right subtees should be same (as in mirror)

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def dfs(left, right):
        if not left and not right:
            return True
        # if one of ghe trees is none -> false
        if not left or not right:
            return False
        # check inside children mirror each other: left.right vs right.left AND The outside children mirror each other: left.right vs right.left
        return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
    return dfs(root.left, root.right)
    

# Is Same Tree
# if both trees are identical -> true, else: false
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


# Balanced Binary Tree
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if node is None:
            return [True, 0]
        
        left, right = dfs(node.left), dfs(node.right)
        # if left, right and from the root is balanced
        balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balance, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]

#Returning [isBalanced, height] together:
#Lets check balance, Avoids recalculating heights


###############################################################
# PHASE 4: Global Variables – Track Max/Min/Longest
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Diamenter of Binary Tree
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node):
        if node is None:
            return 0
        left, right = dfs(node.left), dfs(node.right)
        nonlocal res
        res = max(res, left + right)
        # returns the height 
        return 1 + max(left, right)
    dfs(root)
    return res

#  Maximum Path Sum


