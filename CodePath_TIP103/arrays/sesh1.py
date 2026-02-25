def words_with_char(words, x):
	res = []
	for i, word in enumerate(words):
		if x in word:
			res.append(i)
	return res

words = ["batman", "superman"]
x = "a"
#print(words_with_char(words, x))

# 2 

"""
def hulk_smash(n):
	ans = []
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			ans.append("HulkSmash")
		elif 
		
        elif 

        else:
"""

def shuffle(message, indices):
    res = [''] * len(message)
    for i, c in enumerate(message):
        idx = indices[i]
        res[idx] = c
    return ''.join(res)
	
message = "evil"
indices = [3, 1, 2, 0]
#print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
#print(shuffle(message, indices))

"""
The Riddler is planning to leave a coded message to lead Batman into a trap. Write a function shuffle() that takes in a string, the Riddler's message, and encodes it using an integer array indices.
The message will be shuffled such that the character at the ith position in message moves to index indices[i] in the shuffled string. You may assume len(message) is equal to the len(indices).
"""

"""P4: Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.

Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.

Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.

Note that meals from the same pack can be distributed into different boxes."""
def minimum_boxes(meals, capacity):
	# sort in desc
	capacity.sort(reverse=True)
	
	total = sum(meals)
	box = 0
	if total <= 0:
		return box
	for cap in capacity:
		if total <= 0:
			return box
		total -= cap
		box += 1
	return box if total <= 0 else -1
#Time:  (m +  nlogn)
#Space: 1

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
#print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
#print(minimum_boxes(meals, capacity))

'''
The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.'''
def wealthiest_customer(accounts):
	# interate over account indexes
	    # iterate over each $ in each account to sum the sum
        # total = 
    # return [acount[i], best]
    best_index = 0
    best_sum = sum(accounts[0])
    
    for index, account in enumerate(accounts[1:], start=1):
        cur = sum(account)
        if best_sum < cur:
            best_sum = cur
            best_index = index
    return [best_index, best_sum]
# time: mn, space 1	
    
	

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
#print(wealthiest_customer(accounts)) # [0, 6]

accounts = [
	[1, 5], # 6
	[7, 3], # 10
	[3, 5]  # 8
]
#print(wealthiest_customer(accounts)) # [1, 10]

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
#print(wealthiest_customer(accounts)) # [0, 17]

def smaller_than_current(nums):
	# sort nums 
	sorted_nums = sorted(nums)
	rank = {}
	for i, num in enumerate(sorted_nums):
		if num not in rank:
			rank[num] = i
	res = []
	for num in nums:
		res.append(rank[num])
	return res 
	

nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums)) # [4, 0, 1, 1, 3]

nums = [6, 5, 4, 8] #[2, 1, 0, 3]

print(smaller_than_current(nums))

nums = [7, 7, 7, 7] # 0,0,0,0
print(smaller_than_current(nums))