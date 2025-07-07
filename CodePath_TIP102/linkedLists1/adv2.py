# !!!!
# node consists of a value, and pointer or reference variable to the next node in the list.
# Mock

 # Middle of LL


# Reverse LL
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next_node = cur.next 
            cur.next = prev
            prev = cur
            cur = next_node
        return prev


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        newHead = ListNode()
        head = newHead
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return newHead.next
        


# Problem 1
# greatest Node
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

def find_max(head):
    if not head:
        return None
    maxV = head.value
    cur = head.next
    while cur:
        if cur.value > maxV:
            maxV = cur.val
        cur = cur.next
    return maxV



head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
#print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
#print(find_max(head2))


# ------------
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

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso 
#print_linked_list(remove_tail(head))







#head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
#print_linked_list(delete_dupes(head)) # 1 -> 2 -> 4 -> 5
# P 4
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

#print(has_cycle(peach))

# --- Problem 5 ---
#  Remove Nth Node From End of List
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

def remove_nth_from_end(head, n):
    length = 0
    cur = head
    re = head

    while cur:
        cur = cur.next
        length += 1

    if length == n:
        return head.next
    
    cur2 = head
    for _ in range(length-n-1):
        cur2 = cur2.next
    cur2.next = cur2.next.next
    return head

### 1 PASS 2 POINTER APPROACH
# Leetcode 19, Remove nth from end of list (Medium)

def remove_nth_from_end(head, n):
    dummy = ListNode(0,head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n-=1
    while right:
        left = left.next
        right = right.next
    # delete
    left.next = left.next.next
    return dummy.next


head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))


#apple -> cherry -> orange -> pear
#Rainbow Trout

#Example 3 Explanation: The last example returns an empty list.

# Problem 6
#Reverse K elems
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
        
def reverse_first_k(head, k):
    cur = head
    count = 0
    prev = None
    if not head or k <= 1:
        return head
    while cur and count < k:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
        count+=1
    head.next = cur
    return prev



head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

#print_linked_list(reverse_first_k(head, 3))


#orange -> cherry -> apple -> peach -> pear