# Intersection of 2 lists Leetcode 160 (Easy)
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        a = headA
        b = headB
        while b is not a:
            b = b.next if b else headA
            a = a.next if a else headB
        return b

# Problem 1: Next in Queue
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    
    def dequeue(self):
        if self.is_empty():
            return None
        removed_val = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_val

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value


#Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
#print("Peek: ", q.peek()) 
#Remove elements from the queue
#print("Dequeue: ", q.dequeue()) 
#print("Dequeue: ", q.dequeue()) 
#Check if the queue is empty
#print("Is Empty: ", q.is_empty()) 
#Remove the last element
#print("Dequeue: ", q.dequeue()) 
#Check if the queue is empty
#print("Is Empty:", q.is_empty()) 

#('Love Song', 'Sara Bareilles') -> ('Ballad of Big Nothing', 'Elliot Smith') 
# -> ('Hug from a Dinosaur', 'Torres')
# Peek:  ('Love Song', 'Sara Bareilles')
# Dequeue:  ('Love Song', 'Sara Bareilles')
# Dequeue:  ('Ballad of Big Nothing', 'Elliot Smith')
# Is Empty:  False
# Dequeue:  ('Hug from a Dinosaur', 'Torres')
# Is Empty: True

# Problem 2 
# LC LeetCode 1669: Merge In Between Linked Lists

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    # Step 1: Find the (a-1)th node, i.e., the node before 'a'
    prev_a = playlist1
    for _ in range(a-1):
         prev_a = prev_a.next
    # Step 2: Find the bth node
    node_b = prev_a
    for _ in range(b-a+2):
         node_b = node_b.next

    after_b = node_b

    # Step 3: Connect prev_a to the head of playlist2
    prev_a.next = playlist2
    
    # Step 4: Traverse to the end of playlist2
    tail = playlist2
    while tail:
         tail = tail.next
    # Step 5: Connect the last node of playlist2 to the node after b
    tail.next = after_b

    return playlist1
# 1-2-3-4  => 1-2   4-3  => 1-4-2-3

# 143 Reorder List Leetcode (Medium)

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    if not playlist or not playlist.next:
        return playlist
    slow = playlist
    fast = playlist
    # middle 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None # delete arrow to next node
    prev = None

    # reverse 2nd part
    while middle:
       nxt = middle.next
       middle.next = prev
       prev = middle
       middle = nxt
    
    l1 = playlist
    l2 = prev
    while l2:
        # save the reference
        nxt_l1 = l1.next
        nxt_l2 = l2.next
        # take 1 from l1 next from l2
        l1.next = l2
        l2.next = nxt_l1
        # move pointers 
        l1 = nxt_l1
        l2 = nxt_l2

    return playlist
playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

#print_linked_list(shuffle_playlist(playlist1))
#print_linked_list(shuffle_playlist(playlist2))

# Double Linstening Count
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def double_listeners(monthly_listeners):
    # reverse list
    cur = monthly_listeners
    prev = None
    while cur:
         nxt = cur.next
         cur.next = prev
         prev = cur
         cur = nxt
    # double each val
    cur = prev
    carry = 0
    tail = 0
    while cur:
        total = cur.value * 2 + carry
        cur.value = total % 10 # val i store
        carry = total // 10 # what i pass to the next digi
        tail = cur
        cur = cur.next
    if carry > 0:
        tail.next = Node(carry)
        

    # reverse back 
    current = prev
    previous = None
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    return previous

monthly_listeners1 = Node(1, Node(8, Node(9))) # 189
monthly_listeners2 = Node(9, Node(9, Node(9))) # 999

print_linked_list(double_listeners(monthly_listeners1))
print_linked_list(double_listeners(monthly_listeners2))
#Example Output:

#3 -> 7 -> 8
#Example 1 Explanation: 189 * 2 = 378

#1 -> 9 -> 9 -> 8
#Example 2 Explanation: 999 * 2 = 1998