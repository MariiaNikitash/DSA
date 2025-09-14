'''
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        def length(w):
            length_w = len(w)
            res = str(length_w) + '#' + w
            return res
        
        for word in strs:
            result.append(length(word))
        return ''.join(result)
        #4#love#8neetcode
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1 # increment till #
            # convert digit to a int so we can fast forward for that many letters
            length = int(s[i:j]) # so for xample '4#love - len is 4 
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length # shift i to next 
        return res

#Encode: O(m) time, O(m) space
#Decode: O(m) time, O(m + n) space (to rebuild the list of n words)

# _______________________________________
#### ok it doesnt work with other digits ...
# def encode(strs):
#         result = []
#         def length(w):
#             length_w = len(w)
#             res = '#' + str(length_w) + w
#             return res
#         
#         for word in strs:
#             result.append(length(word))
#         return ''.join(result)
# 
# 
# def decode(s):
#     res = []
# 
#     num_list = s.split('#')
#     for w in num_list:
#         res.append(w[1:])
#     return res
# 
# 
# test = ["neet","code","love","you"]
# print(type(encode(test)))
# print(encode(decode(test)))
# 
# hello = 'hello'
# print(hello[1:])




