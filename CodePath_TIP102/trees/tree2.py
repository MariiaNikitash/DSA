from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    # Is balanced Tree
class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def smallest_to_largest_recursive(pearls):
    sorted_list = []
    
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)   
            sorted_list.append(node.val) 
            inorder_traversal(node.right)  
    
    inorder_traversal(pearls)
    return sorted_list

def smallest_to_largest_iterative(pearls):
    #stack = []
    #sorted_list = []
    pass


from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
    if not values:
        return None
  
    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item
  
    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
          node = queue.popleft()
          if index < len(values) and values[index] is not None:
              left_key, left_value = get_key_value(values[index])
              node.left = TreeNode(left_value, left_key)
              queue.append(node.left)
          index += 1
          if index < len(values) and values[index] is not None:
              right_key, right_value = get_key_value(values[index])
              node.right = TreeNode(right_value, right_key)
              queue.append(node.right)
          index += 1
    
    return root

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def locate_treasure(grotto, treasure):
    if not grotto:
        return False
    if grotto.val > treasure:
        return locate_treasure(grotto.left, treasure)
    elif grotto.val < treasure:
        return locate_treasure(grotto.right, treasure)
    else:
        return True



"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper"))  
print(locate_treasure(grotto, "Thingamabob")) 


# -----------------------------------------------------------------
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def add_treasure(grotto, new_item):
    if not grotto:
        return False
    if grotto.val > new_item:
        return locate_treasure(grotto.left, new_item)
    elif grotto.val < new_item:
        return locate_treasure(grotto.right, new_item)
    else:
        return True


"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob")) 

# -----------------------------------------------------------------
# Problem 3: add node at leaf
"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob")) 

['Snarfblat', 'Gadget', 'Whatzit', 'Dinglehopper', 'Gizmo', None, 'Whozit']
'''
               Snarfblat
            /             \
        Gadget            Whatzit
       /     \           /       \
Dinglehopper Gizmo  Thingamabob  Whozit
'''

# -----------------------------------------------------------------
# Problem 4: 
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_species(ecosystem, name):
    pass

"""
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass
"""
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(ecosystem)

# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))

#['Dugong', 'Brain Coral', 'Giant Clam', None', 'Clownfish', None, 'Seagrass']
'''
Explanation:
The resulting tree structure:
             Dugong
            /      \
      Brain Coral  Giant Clam
              \            \
           Clownfish    Seagrass '''


# rooot node val is equal to sum of ALL childs
# if so -> True
# Otherwise _> False
def root_equals_sum_of_descendants(root):
    # Write your code here
    if not root:
        return True
    def dfs(node):
        if not node:
            return 0
        return node.val + dfs(node.left) + dfs(node.right) 
    return root.val == dfs(root.left) + dfs(root.right)
