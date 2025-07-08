# OPP and LL 
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.neighbor = neighbor
        self.furniture = []
#apollo = Villager("Apollo", "Eagle", "pah")
#print(apollo.name)
#print(apollo.species) 
#print(apollo.catchphrase)
#print(apollo.furniture)

    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

# 3, 4
def of_personality_type(townies, personality_type):
    res = []
    for v in townies:
        if v.personality == personality_type:
            res.append(v.name)
    return res
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

#print(of_personality_type([isabelle, bob, stitches], "Lazy"))  # ['Bob', 'Stitches']
#print(of_personality_type([isabelle, bob, stitches], "Cranky")) # []


def message_received(start_villager, target_villager):
    current = start_villager
    while current is not None:
        if current == target_villager:
            return True
        current = current.neighbor 
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

#print(message_received(isabelle, kk_slider))
#print(message_received(kk_slider, isabelle))


# P 5
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

#print(print_linked_list(kk_slider))
#===========================



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
        print(f"Aw! Better luck next time!")
        return None
    current = head
    print(f"I cought a {head.fish_name} ")
    while current:
        current = current.next
    return head.next


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

#print_linked_list(fish_list)
#print_linked_list(catch_fish(fish_list))
#print(catch_fish(empty_list))

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    count = 0
    cur = head
    goal = 0
    while cur:
        count+=1
        if cur.fish_name == fish_name:
            goal +=1
        cur = cur.next
    if count == 0:
        return 0.0
    res = goal / count
    return round(res,2)

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
#print(fish_chances(fish_list, "Dace"))
#print(fish_chances(fish_list, "Rainbow Trout"))

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    if not head:
        return Node(new_fish)
    current = head
    while current.next:
        current = current.next
    current.next = Node(new_fish)

    return head
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
#print_linked_list(restock(fish_list, "Rainbow Trout"))

# Remove val
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
# When i work with deleteing i have to check the node in fron t so i do wjile cur.next
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  
            return head  
        current = current.next

    return head

head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

print_linked_list(remove_by_value(head, "Waluigi"))

# Problem 3: Partition List Around Value
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
    pass


head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(head, 3))


#1 -> 2 -> 2 -> 4 -> 3 -> 5