def is_palindrome(s):
    
    r,l = 0, len(s)-1
    while r < l:
        if s[r] != s[l]:
            return False
        r+=1
        l-=1
    return True

s = "madam"
#print(is_palindrome(s)) # T

s = "madamweb"
#print(is_palindrome(s)) # F


#P 3

def squash_spaces(s):
    res = []
    cur = []
    for c in s:
        if c != " ":
            cur.append(c)
        elif cur:
            res.append("".join(cur))
            cur = []       
    if cur:
        res.append("".join(cur))
    return " ".join(res)



s = "   Up,     up,   and  away! "
#print(squash_spaces(s)) #"Up, up, and away!"

s = "With great power comes great responsibility."
#print(squash_spaces(s)) # "With great power comes great responsibility."

# P4 2ptr sum

def two_sum(nums, target):
    l,r = 0, len(nums)-1
    while r < l:
        if nums[r] + nums[l] == target:
            return [l,r]
        elif nums[r] + nums[l] < target:
            l -=1
        else:
            r +=1


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target)) # [0, 1]

nums = [2, 7, 11, 15]
target = 18
two_sum(nums, target) # [1, 2]




def three_sum(nums):
    # if all 0 0 0 -> 
    # sort arr
    res = []
    nums.sort()
    l,r = 0, len(nums)-1
    for i in range(len(nums)):
        while l < r:
            if nums[l] + nums[r] + nums[i] == 0:
                res.append([nums[l], nums[r], nums[i]])

                l+=1
                r-=1
            elif nums[l] + nums[r] + nums[i] < 0:
                l +=1
            else:
                r-=1
            
    return res

# -4, -1, -1, 0,1, 2
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
three_sum(nums)