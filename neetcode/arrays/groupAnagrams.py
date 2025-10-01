from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = defaultdict(list)
        
        for w in strs:
            key = tuple(sorted(w))
            if key not in dic:
                dic[key].append(w)
            else:
                dic[key].append(w)

     
        for v in dic.values():
            res.append(v)
        return res
    
# time O(M * nlogN), For each word of length m, sorting takes O(m log m).

#For n words total → O(n · m log m).
# space (M*N)
# Dictionary stores up to n words across groups → O(n · m) total for the output.


#Solution with ord function
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord("a")] +=1
            key = tuple(count)
            if key not in dic:
                dic[key] = [w]
            else:
                dic[key].append(w)
        
        return list(dic.values())
    
#time: N*M
# space: N*M