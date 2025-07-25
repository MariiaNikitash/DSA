# arr to LL
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = Node(val)
        cur = cur.next
    return head


mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

#print_linked_list(arr_to_ll([mario, luigi, peach])) # Mario -> Luigi -> Peach 

#print_linked_list(arr_to_ll([peach]))



# Problem 2 
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Function with a bug!
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  # fixed
            return head  
        current = current.next

    return head

# Problem 3: Partition List Around Value
# partitions the linked list around val such that all nodes
# with values less than val come before nodes with values greater than or equal to val.
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

def partition(head, val):
    less_head, greater_head = Node(0), Node(0)
    less, greater = less_head, greater_head

    cur = head
    while cur:
        if cur.value < val:
            less.next = cur
            less = less.next
        else:
            greater.next = cur
            greater = greater.next
        cur = cur.next
    
    greater.next = None  # Important for cycles
    less.next = greater_head.next
    return less_head.next

# Problem 4: Middle Match

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

def middle_match(head, val):
    if not head:
        return False
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.value == val


kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))
tournament_tracks = Node("Rainbow Road", Node("Bowser Castle", Node("Sherbet Land", Node("Yoshi Valley"))))

#print(middle_match(kart_choices, "Wild Wing")) # T
#print(middle_match(tournament_tracks, "Bowser Castle")) # F

# reverse List
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


def reverse(head):
    cur = head
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))

#print_linked_list(reverse(kart_choices))



# ====================================================
# Is summentrical Linked List
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

def is_symmetric(head):
    if not head or head.next is None:
        return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse 2nd half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    # compare 2 parts
    left, right = head, prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True



head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1)) # T
print(is_symmetric(head2)) # F



