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
    return [root.val] + right_vine(root.right)


# or with a helper
def right_vine(root):
    res = []
    def helper(node):
        if not node:
            return []
        res.append(node.val)
        helper(node.right)
    
    helper(root)
    return res


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

#print(sum_inventory(inventory))


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
    /   /
   -     *
  / \   / /
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

#print(helper(root))


# Add all the leaf nodes to array
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_most_specific(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    
    l = get_most_specific(root.left)
    r = get_most_specific(root.right)

    return l + r


"""
           Plantae
          /       /
         /         /
        /           \ 
Non-flowering     Flowering
   /      \       /        /
Mosses   Ferns Gymnosperms Angiosperms
                             /     /
                        Monocots  Dicots
"""
plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

#print(get_most_specific(plant_taxonomy))

# =================
#Problem 7
# count trees greater threshold
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0
    count = 1 if root.val > threshold else 0
    count += count_old_growth(root.left, threshold)
    count += count_old_growth(root.right, threshold)

    return count


"""
     100
     /  /
    /    /
  1200  1500
  /     /  /
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))



# Same Treees 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and not root2 or root2 and not root1:
        return False
    if root1.val != root2.val:
        return False
    
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

"""
      1                1
     / \              / \
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))