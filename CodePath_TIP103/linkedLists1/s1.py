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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# Add code here to link the above nodes
print_linked_list(kk_slider)

#P
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if not head:
        print("Aw! Better luck next time!")
        return None
    
    print(f"I caught a {head.fish_name}!")
    head = head.next

    

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    if not head:
        return None
    dummy = Node()
    prev = dummy
    dummy.next = head
    count = 1
    cur = head

    while cur.next:
        if count == target-1:
            tmp = prev.next
            prev.next= cur.next
            next_node = cur.next.next



def increment_rank(head, target):
    if not head or target == 1:
        return head

    count = 1
    dummy = Node("")
    dummy.next = head
    prev = dummy
    curr = head

    while curr and curr.next:
        if count == target - 1:
            prev.next = curr.next
            next_node = curr.next.next
            curr.next.next = curr
            curr.next = next_node
            return dummy.next

        prev = curr
        curr = curr.next
        count += 1

    return dummy.next

        






racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 