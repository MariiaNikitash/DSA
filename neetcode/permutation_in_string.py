#Permutation in String
# LC 567 (Medium)
#You are given two strings s1 and s2.

#Return true if s2 contains a permutation of s1, or false otherwise.
# That means if a permutation of s1 exists as a substring of s2, then return true.

#Both strings only contain lowercase letters.

#Example 1:

#Input: s1 = "abc", s2 = "lecabee"

#Output: true

#Example 2:

#Input: s1 = "abc", s2 = "lecaabee"

#Output: false


# The brute force would be:
#  sort s1 and get the len s1
# iterate through index (len s2 - len s1 + 1) times
# create a window = [index: index+k]
#then compare if sorted window == sorted s1 and return True else fasle

# time would be:
# n = len s1
# m = len s2
# O(m * n * n log n)
def checkInclusion(s1, s2):
    sorted_s1 = sorted(s1)   # O(n log n)
    k = len(s1)
    for i in range(len(s2)-k+1):  # loop runs O(m - n + 1) ≈ O(m)
        window = s2[i:i+k]   # slice is O(n)
        if sorted(window) == sorted_s1:  # sorting window: O(n log n)
            return True
    return False
print(checkInclusion("abc", "lecabee"))



# Hash map solution
from collections import Counter
def perm(s1, s2):
    if len(s1) > len(s2):
        return False
    countS1 = Counter(s1)
    windowCount = Counter(s2[: len(s1)])

    if countS1 == windowCount:
        return True
    for i in range(len(s1), len(s2)):
        # Add new char to the window
        windowCount[s2[i-len(s1)]] +=1

        # Remove char going out of window
        left_char = s2[i - len(s1)]
        windowCount[left_char] -= 1
        if windowCount[left_char] == 0:
            del windowCount[left_char]  # Clean up to keep the dicts equal when needed

        if windowCount == countS1:
            return True

    return False

# NOW 26-Array Version:
# Time: O(n)
# Space: O(1)
def perm_str(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] +=1
        s2Count[ord(s2[i]) - ord('a')] +=1 
    
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] +=1
        if s1Count[index] == s2Count[index]:
            matches +=1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
        

        index = ord(s2[l]) - ord('a')
        s2Count[index] -=1
        if s1Count[index] == s2Count[index]:
            matches +=1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l+=1
    return matches == 26

print(perm_str("abc", "lecabee"))