class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
# get the right path and append to result
def right_vine(root):
    if  not root:
        return []
    res = []
    node = root
    while node:
        res.append(node.val)
        node = node.right

    return res
# -------------------------------------------------------

# do same thing but recursively
def right_vine(root):
    if  not root:
        return []
    res = []
    return right_vine()


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    if not root:
        return []
    res = []
    def helper(node):
        if not node:
            return
        if node.left:
            helper(node.left)
        if node.right:
            helper(node.right)
        res.append(node.val)
    helper(root)

    return res

            
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

#print(survey_tree(magnolia))

# -------------------------------------------------------
# Sum Node Values
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    summ = 0
    def add_vals(node):
        nonlocal summ
        if not node:
            return
        summ += node.val
        add_vals(node.right)
        add_vals(node.left)

    add_vals(inventory)
    return summ


# or without a helper 
def sum_inventory(inventory):
    if not inventory:
        return 0
    return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))


# -------------------------------------------------------
# Problem 5

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# calculate_yield(root 
def helper(node):
    if not node:
        return
    if not (node.left or node.right):
        return node.val
    if node.val == '+':
        return helper(node.left) + helper(node.right)
    if node.val == '-':
        return helper(node.left) - helper(node.right)
    if node.val == '*':
        return helper(node.left) * helper(node.right)
    if node.val == '/':
        return helper(node.left) / helper(node.right)

    return helper(root)
    
"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2

 22
Explanation:
- 4 - 2 = 2
- 10 * 2 = 20
- 2 + 20 = 22
"""
root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(helper(root))