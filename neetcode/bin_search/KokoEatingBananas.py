# Koko Eating Bananas 
'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and
eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can
not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Ex:
Input: piles = [1,4,3,2], h = 9
Output: 2

U: you are given an arr piles of bananas each pile has n bananas, I am also given an int h, which represents num
of hours i have to eat all the bananas. 
I need to return an int K which is minimum speed i can eat all bananas from each pile
P:
Use bin search, where left start on 1 and r is biggest num of bananas in the pile
iterate while l<= r and compute the middle value k, then divide number of bananas in a pile by k, do it for every pile in bananas
then if hours are smaller then h, you shift right to the k-1 and try to look for even smaller val, and meanvile update
the result to this amount of hours,  otherwise if hours is more then H, means it is too slow so you shift l = k+ 1
at the end we ret best k  
'''

class Solution:
    def minEatingSpeed(self, piles, h):
        l,r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res