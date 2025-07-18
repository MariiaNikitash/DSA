# Recursion

def repeat_hello(n):
	if n > 0:
		print("Hello", n)
    
		repeat_hello(n - 1)
		
#repeat_hello(5)

# Problem: 2
#Time Complexity: O(n) because we make n recursive calls.
#Space Complexity: O(n) because each recursive call adds a layer to the call stack, using more memory.
def factorial(num):
    # Action to repeat
    print(f"Count {num}")
    # Base case
    if num == 0:
        return 1
    #Recursive case
    else:
       return num * factorial(num-1)

#print(factorial(5))

# Iteravely it would take up O(1) space since no extra DS is used
def fac(n):
    res = 1
    for i in range(1, n+1):
        res *=i
    return res
#print(fac(5))


# Problem 3: Recursive Sum
def sum_list(lst):
    if lst == []:
        return 0
    
    return lst[0] + sum_list(lst[1:])

#print(sum_list([1, 2, 3, 4]))

# The recursive calls stack up the additions, and they
# don’t happen all at once. The function keeps calling itself until it
# reaches the base case ([]), then starts adding the results back together.

# Problem 4: Recursive Power of 2
# Time Complexity: O(log n) because each recursive call reduces the problem size by half.
#Space Complexity: O(log n) due to the recursion stack depth, also reducing by half each time.

def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

#print(is_power_of_two(5))
#print(is_power_of_two(8))

# Problem 5: Binary Search 1
def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1 
	# While left pointer is less than right pointer:
    while left < right: 
        mid = (left + right) // 2
        if lst[mid] == target:
             return mid
        elif lst[mid] > target:
             right = mid -1
        else:
             left = mid + 1
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
#print(binary_search(lst, target))
# Expected Output: 5
# Explanation: 11 has index 5 in the list

# Problem 6:
def find_last(lst, target):
    left = 0
    right = len(lst) -1
    res = -1
    while left < right: 
        mid = (left + right) // 2
        if lst[mid] == target:
            res = mid
            left = mid + 1
        elif lst[mid] > target:
             right = mid -1
        else:
             left = mid + 1
    return res

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
#print(find_last(lst, target))
# Expected Output: 6
# Explanation: The second (last) occurrence of 11 has index 6 in the list


# Problem 7
def find_floor(lst, x):
    low, high = 0, len(lst)-1
    floor = None
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] <= x:
            floor = lst[mid]    # store this value, it's valid
            low = mid + 1       # go right for a better (closer to x) one
        else:
            high = mid - 1
    return floor

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
#print(find_floor(lst, x))


# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.
