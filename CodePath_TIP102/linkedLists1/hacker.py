# Create Linked List
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for val in values[1:]:
        cur.next = Node(val)
        cur = cur.next
    return head


# Insert in the position def insert(head, value, position):
def insert(head, value, position):
    new_node = ListNode(value)

    # Insert at the head
    if position == 0:
        new_node.next = head
        return new_node

    cur = head
    count = 0

    while cur and count < position - 1:
        cur = cur.next
        count += 1

    # Insert in the middle or end
    new_node.next = cur.next
    cur.next = new_node

    return head

Example 1: Insert in the middle
Input:
Linked list: 1 -> 2 -> 4
Insert value: 3
Position: 2

Output:
1 -> 2 -> 3 -> 4 -> None


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Complete the 'most_primes_list' function below.
#
# The function is expected to return a SinglyLinkedListNode.
# The function accepts two SinglyLinkedListNode parameters: head_a and head_b.
#
def most_primes_list(head_a, head_b):
    countA, countB = 0,0
    curA = head_a
    curB = head_b
    while curA:
        if is_prime(curA.data):
            countA +=1
        curA = curA.next
    while curB:
        if is_prime(curB.data):
            countB +=1
        curB = curB.next
    
    if countA >= countB:
        return head_a
    else:
        return head_b
    

# Palindrome Linked list!!! 
# Add 2 numbers
