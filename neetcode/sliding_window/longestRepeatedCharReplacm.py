'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.


Plan: maintain a window and keep track its len

to make the whole window one letter, the best choice is the most frequent letter already there—change all others to it.
So changes needed = window size − that max frequency.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # If replacements needed > k, shrink from the left until valid
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1
            res = max(res, r-l+1)
        return res
    
# time O(n)
# space O(n)