class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # make. dict for nums
        # val : amount of times it appared
        dic ={}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        # iterate over the val, values in a dict
        n = len(nums)
        for k,v in dic.items():
            if v > (n / 2):
                return k
        # get the len of nums
        # check if val appears > n / 2 times
        #return this value