class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        res = []
        for k,v in dic.items():
            if v > (len(nums)/3):
                res.append(k)
        return res
    
#Time , space O