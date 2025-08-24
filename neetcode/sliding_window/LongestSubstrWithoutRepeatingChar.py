'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0
        for r in range(len(s)):    # right pointer moves n times
            while s[r] in charSet: # left pointer removes until valid
                charSet.remove(s[l])
                l+= 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
# Time: O(N) 
# Even though there’s a nested while, each character is processed at most twice:

#Once when the right pointer r adds it.

#Once when the left pointer l removes it.

#Since l and r only move forward, never backward → total moves ≤ 2n.
#That’s O(n).#

# Space: O(N)