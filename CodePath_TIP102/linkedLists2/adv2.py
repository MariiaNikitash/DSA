#class Node:
#	def __init__(self, value, next=None):
#		self.value = value
#		self.next = next
#
## For testing
#def print_queue(head):
#    current = head.front
#    while current:
#        print(current.value, end=" -> " if current.next else "")
#        current = current.next
#    print()
#
#class Queue:
#    def __init__(self):
#        self.front = None
#        self.rear = None
#    
#    def is_empty(self):
#        return self.front is None
#
#    def enqueue(self, value):
#        temp = Node(value)
#
#    
#    def dequeue(self):
#        if self.is_empty():
#            return None
#        ans = self.front.value
#        self.front = self.front.next
#        if self.front is None
#
#    def peek(self):
#        pass
#
#
##Create a new Queue
#q = Queue()
#
## Add elements to the queue
#q.enqueue(('Love Song', 'Sara Bareilles'))
#q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
#q.enqueue(('Hug from a Dinosaur', 'Torres'))
#print_queue(q)
#
## View the front element
#print("Peek: ", q.peek()) 

# Remove elements from the queue
#print("Dequeue: ", q.dequeue()) 
#print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
#print("Is Empty: ", q.is_empty()) 

# Remove the last element
#print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
#print("Is Empty:", q.is_empty()) 

#('Love Song', 'Sara Bareilles') -> ('Ballad of Big Nothing', 'Elliot Smith') 
# -> ('Hug from a Dinosaur', 'Torres')
# Peek:  ('Love Song', 'Sara Bareilles')
# Dequeue:  ('Love Song', 'Sara Bareilles')
# Dequeue:  ('Ballad of Big Nothing', 'Elliot Smith')
# Is Empty:  False
# Dequeue:  ('Hug from a Dinosaur', 'Torres')
# Is Empty: True


#class Node:
#	def __init__(self, value, next=None):
#		self.value = value
#		self.next = next
#
## For testing
#def print_linked_list(head):
#    current = head
#    while current:
#        print(current.value, end=" -> " if current.next else "")
#        current = current.next
#    print()
#
#def merge_playlists(playlist1, playlist2, a, b):
#    pl1 = playlist1
#    pl2 = playlist2
#    dummy = None
#    count = 0
#    while pl1:
#        if count == a:
#            next_pl1 = pl1.next
#            break
#        count +=1
#        pl1 = pl1.next
#    pl1.next = pl2
#    .next = next_pl1
    

# 1-2-3-4  => 1-2   4-3  => 1-4-2-3


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

