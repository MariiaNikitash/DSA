'''
Happy Number LC 202 (Easy)
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
    

def isHappy(n: int) -> bool:
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1