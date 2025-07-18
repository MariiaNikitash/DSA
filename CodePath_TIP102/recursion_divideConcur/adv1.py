
# Recursion

# Problem 1
def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1
    
    return 1 + count_layers(sandwich[1])


sandwich1 = ["bread",["lettuce",["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

#print(count_layers(sandwich1)) # 4
#print(count_layers(sandwich2)) # 5

'''
helper:
 base case: if len(order) <= 1:
        return order
reverse list from 2nd elem 

'''
'''
           Building the call stack:
        Call 1: helper(['Bagel', 'Sandwich', 'Coffee'])
         → pauses and waits for:
        Call 2: helper(['Sandwich', 'Coffee'])
         → pauses and waits for:
        Call 3: helper(['Coffee'])
         → Base case! Returns ['Coffee']
        
        
        Now the call stack looks like this:
        ⤴ helper(['Bagel', 'Sandwich', 'Coffee']) ← waiting
           ⤴ helper(['Sandwich', 'Coffee']) ← waiting
               ⤴ helper(['Coffee']) ← returned ['Coffee']
        
           ''' 
def reverse_orders(orders):

    def helper(order):
        if len(order) <= 1:
            return order
        return helper(order[1:]) + [order[0]]  # wrap in [] to keep it a list

    order = orders.split(' ')  # split into list of words
    res = helper(order)        # reverse the list recursively
    return ' '.join(res)       # join with space to form final string

#print(reverse_orders("Bagel Sandwich Coffee")) # # str -> Coffe Sandwtch Bagel


# Problem 3: Sharing the Coffee
def can_split_coffee(coffee, n):
    summ = 0
    for c in coffee:
        summ += c
    
    if summ % n == 0:
        return True
    return False
# I cant thunk of recursion here 
#print(can_split_coffee([4, 4, 8], 2))
#print(can_split_coffee([5, 10, 15], 4))

# Problem 4: Combine 2 linked Lists a and b 
'''
input: A: a1-a2-a3-a4
       B: b1-b2-b3
Output: a1-b1-a2-b2-a3-b3-a4
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    next_a = sandwich_a.next
    next_b = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(next_a, next_b)
    
    return sandwich_a
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

#Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
#Bacon -> Bread -> Lettuce -> Tomato




#