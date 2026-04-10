def check_stock(inventory, part_id):
    l,r = 0, len(inventory)-1

    while l <= r:
        m = (l+r) // 2
        if part_id == inventory[m]:
            return True
        elif part_id > inventory[m]:
            l = m + 1
        else:
            r = m - 1
    return False

#print(check_stock([1, 2, 5, 12, 20], 20))
#print(check_stock([1, 2, 5, 12, 20], 100))


# p 2
def check_stock(inventory, part_id):
    
    m = len(inventory) // 2

    if part_id == inventory[m]:
            return True

    if len(inventory) == 1:
         return False
    elif part_id < inventory[m]:
        return check_stock(inventory[:m], part_id)
    
    else:
         return check_stock(inventory[m:], part_id)
    

#print(check_stock([1, 2, 5, 12, 20], 20))
#print(check_stock([1, 2, 5, 12, 20], 100))

def find_frequency_positions(transmissions, target_code):
    def first():  
        first = -1  
        l,r = 0, len(transmissions)-1
        while l <= r:
            m = (l+r) // 2
            if target_code == transmissions[m]:
                first = m
                r = m -1

            elif target_code > transmissions[m]:
                l = m + 1
            else:
                r = m - 1
        return first 
    
    def last():  
        last = -1  
        l,r = 0, len(transmissions)-1
        while l <= r:
            m = (l+r) // 2
            if target_code == transmissions[m]:
                last = m
                l = m + 1
            elif target_code > transmissions[m]:
                l = m + 1
            else:
                r = m - 1
        return last

    return (first(), last())


print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))