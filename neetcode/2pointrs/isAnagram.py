'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for i in s:
            if i not in dicS:
                dicS[i] = 1
            else: 
                dicS[i] += 1

        for i in t:
            if i not in dicT:
                dicT[i] = 1
            else: 
                dicT[i] += 1
        return dicS == dicT