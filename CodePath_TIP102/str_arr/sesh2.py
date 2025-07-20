# SESSION 2

def transpose(matrix):
   row = len(matrix)
   col = len(matrix[0])
   result = [[0] * row for _ in range(col)]

   for r in range(row):
       for c in range(col):
           result[r][c] = matrix[r][c]
   return result
#Time/Space O(m * n)   

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(transpose(matrix))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

def reverse_list(lst):
    p1 = 0
    p2 = len(lst) - 1

    while p1 < p2:
        lst[p1],lst[p2] = lst[p2], lst[p1]
        p1+=1
        p2-=1
    return lst
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
#print(reverse_list(lst))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*


def remove_dupes(items):
    l = 0
    while l < len(items)-1:
        if items[l] == items[l+1]:
            items.pop(l+1)
        else:
            l+=1
    return items


items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
#print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
#print(remove_dupes(items))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*


# in 2 ptrs use if-elif block bc i only want to execute 1 line 
def sort_by_parity(nums):
    l = 0
    r = len(nums) -1
    while l<r:
        if nums[l] % 2 == 0:
            l+=1
        elif nums[r] % 2 == 1:
            r-=1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    return nums

#O(n) time, O(1) space
nums = [3, 1, 2, 4]
#print(sort_by_parity(nums))

nums = [0]
sort_by_parity(nums)

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*


# Container with most water
def most_honey(height):
    max_area = 0
    l,r = 0, len(height)-1
    while l < r:
        area = (r-l) * min(height[l], height[r])
        max_area = max(max_area, area)
        if height[r] > height[l]:
            l +=1
        else:
            r-=1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#print(most_honey(height))

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# Merge Intervals
#Problem 6: Merge Intervals
#Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key= lambda x: x[0])
    merged = [intervals[0]] #[1,3]
    for start, end in intervals[1:]:
        # Get the end of the last merged interval
        last_end = merged[-1][1] #3
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            intervals.append([start,end])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#print(merge_intervals(intervals))
#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# ============= Set 2 ============

# Matrix Addition 
# func accepts 2 n x m matrices and returns n x m matrix sum of vals from matrixes
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    sum_matr = []

    for _ in range(rows): # makes a matrix of 0s
        sum_matr.append([0] * cols)
    
    for i in range(rows):
        for j in range(cols):
            sum_matr[i][j] = matrix1[i][j] + matrix2[i][j]
    return sum_matr

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

#print(add_matrices(matrix1, matrix2))



# ---------  !!! Hackerrank !!! ----
#Needle
def find_needle(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) +1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*

# can place flowers
# Sliding window 
def canPlaceFlowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]
    count = 0

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1

    return count >= n

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*



# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # N
        stack = [] # S
        res = [] # S
        for w in words: # N 
            stack.append(w)
        while stack: # N 
            res.append(stack.pop())
        return " ".join(res) # N
    

# or with 2 poinres 
class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()  
        l,r = 0, len(word) -1
        while l < r:
            word[l], word[r] = word[r], word[l]
            l+=1
            r-=1
        return " ".join(word)
    

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Reverse words in string 2
'''
input: ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
outpu: ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

have a helper to reverse using 2 ptrs
interate over len of list
create a word strt var
track if pointer idx lands on ' ' then call reverse function and shift idx after ' ' , update word strt var
now we have reversed the letters in words 
finally we have to apply reverse function to reverse the whole list 
'''
def reverseWords(strs):
    def revers(word, start, end):
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1

    word_start = 0
    n = len(strs)
    for idx in range(n):
        if strs[idx] == ' ':
            revers(strs, word_start, idx-1)
            word_start = idx + 1
        
        elif idx == n-1:
            revers(strs, word_start, idx)
        
    revers(strs, 0, n-1)
    return strs

input = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
#outp: ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']


print(reverseWords(input))




