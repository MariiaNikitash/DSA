# Get the left most path of TREE

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    if not root:
        return []
    return [root.val] + leftmost_path(root.left) 
    

"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

#print(leftmost_path(system_a)) # ['CaveA', 'CaveB', 'CaveD']
#print(leftmost_path(system_b)) # ['CaveA']


# -------------------
#now iteratively
def leftmost_ph(root):
    if not root:
        return None
    res = []
    while root:
        res.append(root.val)
        root = root.left
    return res

#print(leftmost_ph(system_a)) # ['CaveA', 'CaveB', 'CaveD']

#  -------------------  -------------------  -------------------  -------------------  -------------------  -------------------
# Problem 3:
# return number of nodes in Tree
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_species(node):
    if not node:
        return 0
    return 1+ count_species(node.left) + count_species(node.right) 


"""
         Shark
       /       \  
      /         \
   Grouper     Snapper
   /     \           \  
Conch   Tang       Zooplankton
"""

food_chain = TreeNode("Shark", 
                    TreeNode("Grouper", TreeNode("Conch"), TreeNode("Tang")),
                            TreeNode("Snapper", None, TreeNode("Zooplankton")))

#print(count_species(food_chain))

#  -------------------  -------------------  -------------------  -------------------  -------------------  -------------------
# Problem 4:
# add all nodes to list using preordder traversal

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def explore_reef(root):
    if not root:
        return []
    res = []
    res.append(root.val)
    res += explore_reef(root.left)
    res += explore_reef(root.right)
    return res

"""
         CoralA
        /     \
     CoralB  CoralC
     /   \      
 CoralD CoralE  
"""

reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

#print(explore_reef(reef)) # ['CoralA', 'CoralB', 'CoralD', 'CoralE', 'CoralC']


#  -------------------  -------------------  -------------------  -------------------  -------------------  -------------------
# Problem 5:

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(node):
    pass

"""
        AND
     /      \
   OR       AND
  /  \       /  \
True False True False
"""

root = TreeNode("AND")
root.left = TreeNode("OR")
root.right = TreeNode("AND")
root.left.left = TreeNode(True)
root.left.right = TreeNode(False)
root.right.left = TreeNode(True)
root.right.right = TreeNode(False)
print(get_decision(root))

'''
False
Explanation: 
- Left Subtree Evaluation: True OR False evaluates to True
- Right Subtree Evaluation: True AND False evaluates to False
- Root and children Evaluation: True AND False evaluates to False
'''