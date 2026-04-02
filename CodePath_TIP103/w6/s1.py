
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
    # count the nodes
    n = 0
    cur = protein
    while cur:
        n+= 1
        cur = cur.next
    
    # get the segments
    base = n // k 
    extra = n % k

    res = [] 
    curr = protein
    # build segments
    for i in range(k):
        head = curr
        # check if base 
        part_size = base + 1 if i < k - 1 else extra

        if curr:
            for _ in range(part_size-1):
                curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        res.append(head)
    return res


protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
# Ala -> Gly -> Leu
# Val -> Pro -> Ser
#Thr -> Cys
# base == 3, extra == 2
# k = 0 
    # head = ala 
    # 
parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

