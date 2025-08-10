"""
You are working on an inventory system, which lists all items in alphabetical order. We would like to verify that the system is working correctly.

Write a function that takes in a collection of item name strings in an inventory and returns if the list is in alphabetical order. Treat the items as case insensitive.

Example:
inventory1 = ["candy", "Corn", "Peas"]
checkInventory(inventory1) -> True

inventory2 = ["Clock", "Candy", "Corn", "Peas"]
inventory3 = ["Cards", "Card", "Clothes"]
inventory4 = ["Applesauce", "AppleTV", "Television", "Tractor", "Apple"]
inventory5 = ["Candy", "corn", "Peas"]

All Test Cases:
checkInventory(inventory1) -> True
checkInventory(inventory2) -> False
checkInventory(inventory3) -> False
checkInventory(inventory4) -> False
checkInventory(inventory5) -> True

Complexity analysis variables:
I = Number of items
(Note: Individual item strings have constant length)


"""

# grab the node
# go to the children
# process the original node

inventory1 = ["candy", "Corn", "Peas"]
inventory2 = ["Clock", "Candy", "Corn", "Peas"]
inventory3 = ["Cards", "Card", "Clothes"]
inventory4 = ["Applesauce", "AppleTV", "Television", "Tractor", "Apple"]
inventory5 = ["Candy", "corn", "Peas"]

# [a, b, c, d] -> a <= b, b <= c, 
# lexicographic ordering 
# for i in range(len(inventory)-1):
#     if(inventory[i+1] < inventory[i]) return false

def alphabetical_order(inventory):
    lower_list = [word.lower() for word in inventory] # N
    sorted_list = sorted(lower_list) # nlogn
    return lower_list == sorted_list
    
print(alphabetical_order(inventory1))
print(alphabetical_order(inventory2))
print(alphabetical_order(inventory3))
print(alphabetical_order(inventory4))
print(alphabetical_order(inventory5))


# to optimize 
def checkInventory(inv):
    for i in range(len(inv) - 1):
        if inv[i].lower() > inv[i+1].lower():
            return False
    return True