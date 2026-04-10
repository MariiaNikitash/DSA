def count_layers(sandwich):
    if not sandwich:
        return 0
    if len(sandwich) == 1:
        return 1
    return 1 + count_layers(sandwich[1])

sandwich1 = [['bread']]
sandwich2 = ['bread', 'lettuce', ['tomato']]

#print(count_layers(sandwich1))
#print(count_layers(sandwich2))

#p2

def reverse_orders(orders):
    words = orders.split()

    def rec(words):
        if not words:
            return []
        return [words[-1]] + rec(words[:-1])

    return " ".join(rec(words))


#print(reverse_orders("Bagel Sandwich Coffee"))

#P3

"""The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() that accepts a list of integers coffee representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

"""
def can_split_coffee(coffee, n):
    def helper(arr):
        if not arr:
            return 0
        return arr[0] + helper(arr[1:])

    return helper(coffee) % n == 0
print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))


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
    sandwich_a.next = merge_orders(sandwich_b, next_a)
    return sandwich_a
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')


print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))