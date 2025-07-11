# Linked Lst Cycle 2 LC Medium
class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
# ===============================================
# Problem 1
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
#def print_linked_list(head):
#    current = head
#    while current:
#       print(current.value, end=" -> " if current.next else "\n")
#        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    current = dna_strand
    
    while current:
        # Retain the first m nodes
        for i in range(1, m):
            if current is None:
                return dna_strand
            current = current.next

        if current is None:
            return dna_strand

        # Now current is at the m-th node
        # We will delete the next n nodes
        temp = current.next
        for j in range(n):
            if temp is None:
                break
            temp = temp.next

        # Connect the m-th node to the node after the n deleted nodes
        current.next = temp

        # Move current to the next retained node
        current = temp

    return dna_strand

#dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

#print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

# 1 -> 2 -> 6 -> 7 -> 11 -> 12
# Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
# (1 -> 2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
# Continue with the same procedure until reaching the tail of the Linked List.

# ===========================================================
# Problem 2: Protein Folding Loop Detection
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    if not protein:
        return []
    slow,fast = protein, protein
    res = []
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return []
    s = slow
    while True:
        res.append(s.value)
        s = s.next
        if s == fast:
            break

    return res

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

#print(cycle_length(protein_head)) # ['Gly', 'Leu', 'Val']

# ===========================================================

# Problem 3: Segmenting Protein Chains for Analysis
#725. Split Linked List in Parts
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def split_protein_chain(protein, k):
    cur = protein
    length = 0
    # get length to later split into k segments
    while cur:
        length+=1
        cur = cur.next
    # find size of each seg
    base_size = length // k 
    extra = length % k # segs with 1 node leftover
    cur = protein
    res = []
    for i in range(k):
        head = cur
        seg_size = base_size + (1 if i < extra else 0)

        for j in range(seg_size - 1):
            if cur:
                cur = cur.next
            
        if cur:
            next_seg = cur.next
            cur.next = None
            cur = next_seg
        
        res.append(head)


    return res

protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

# parts = split_protein_chain(protein1, 3)
# for part in parts:
#     print_linked_list(part)
# 
# parts = split_protein_chain(protein2, 5)
# for part in parts:
#     print_linked_list(part)

# ===========================================================

# Problem 4:
# Leetcode 2130. Maximum Twin Sum of a Linked List (Medium)

# find middle
# reverse second half, starting at the second middle element
# make a variable that stores max sum
# then iterate over both
# add nodes values to cur sum
# compare current sum with max sum
#then return max sum

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

def max_protein_pair_stability(head):
# find middle
    slow=fast=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow
    prev = None
    while middle:
        nxt = middle.next
        middle.next = prev
        prev = middle
        middle = nxt
    # now prev is beginning of list 2

    l1 = head
    l2 = prev
    max_sum = 0
    while l2:
        cur_sum = l1.value + l2.value
        max_sum = max(max_sum, cur_sum)
        nxt1,nxt2= l1.next, l2.next
        l1.next = l2
        l2.next = nxt1

        l1, l2 = nxt1,nxt2
    return max_sum

head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))