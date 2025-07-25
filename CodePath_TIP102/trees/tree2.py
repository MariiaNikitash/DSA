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