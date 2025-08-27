"""
Minimum Window Substring
Solved 
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        res = [-1,-1]
        res_len = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                # pop from left of window
                window[s[l]] -= 1
                # if have is not same as need we decrement
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        # unpack 
        l,r = res        
        return s[l:r+1] if res_len != float('inf') else ""
    
# Time O(n+m) # m == Building the frequency map countT takes O(m)
# O(n) for sliding window over s + O(m) for building/using the target counts = O(n + m)

# Space O(m) where m in num of unique chars in T, So memory grows with the number of unique chars in t (and maybe a few more from s, but bounded by the alphabet size).

