def check_stock(inventory, part_id):
    l,r = 0, len(inventory)-1
    while l <= r:
        mid = (l + r) // 2
        if part_id == inventory[mid]:
            return True
        if inventory[mid] > part_id:
            r = mid - 1
        else:
            l = mid + 1 
    return False


#print(check_stock([1, 2, 5, 12, 20], 20))
#print(check_stock([1, 2, 5, 12, 20], 100))




#34. Find First and Last Position of Element in Sorted Array (Medium)
def find_frequency_positions(transmissions, target_code):
    '''
    
    '''
def search_range(nums, target):
    first = -1
    last = -1

    # 🔍 Find first occurrence
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            first = mid
            r = mid - 1  # go left to find earlier target
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    # 🔍 Find last occurrence
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            last = mid
            l = mid + 1  # go right to find later target
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return [first, last]

#print(find_frequency_positions([5,7,7,8,8,10], 8))
#print(find_frequency_positions([5,7,7,8,8,10], 6))
#print(find_frequency_positions([], 0))

'''
(3, 4)
(-1, -1)
(-1, -1)
'''

def next_greatest_letter(letters, target):
    l, r = 0, len(letters) - 1
    res = letters[0]  # default for wrap-around case

    while l <= r:
        mid = (l + r) // 2

        if letters[mid] <= target:
            l = mid + 1
        else:
            res = letters[mid]
            r = mid - 1

    return res

letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))

def find_closest_planets(planets, target_distance, k):
    pass

planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]

#print(find_closest_planets(planets1, 350, 3))
#print(find_closest_planets(planets2, 25, 2))

#Problems 5,6,7

