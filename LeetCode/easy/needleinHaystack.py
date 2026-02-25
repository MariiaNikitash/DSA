class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0  
        for i in range(len(haystack)-len(needle)+1):
                for j in range(len(needle)):
                    if needle[j] != haystack[i+j]:
                        break
                    if j == len(needle) -1:
                        return i
        return -1

# O(n*m) time, space is constant 
# P.S. practice prob before i start leetcode in java