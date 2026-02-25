# Sum on list

def rec_sum(l):
    if not l:
        return 0
    return l[0] + rec_sum(l[1:])

#print(rec_sum([1,2,3]))
'''
so we go down 
1 + [2,3]
2 + [3]
3 + 0
then we go back up
3
then 2 + 3 = 5
then 1 + 5 = 6

'''

# Problem Reverse a string Recursively
def reverse_string(s):
    if not s:
        return ''
    return reverse_string(s[1:]) + s[0]

#print(reverse_string("hello"))

'''ello + h 
   llo  + e
   lo   + l
   o    + l
   '' +   o
   then we go back up and get olleh '''

# Problem Count difits 
# 123 -> 3 digits
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n//10)
#print(count_digits(232))


# Problem Problem 4: Sum of Digits (Recursively)
def sum_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)
#print(sum_digits(456))


# Is palindrome Recursively 
def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False

    return is_pal(s[1:-1])

#print(is_pal('madam'))


# Multiply 2 nums without using * 
'''
a=3, b=4'
3+3+3+3 = 12
'''
def multiply(a,b):
    if b == 0:
        return 0
    return a+ multiply(a, b-1)

#print(multiply(3,4))

# Count Dpwn
#4-3-2-1
def countdown(n):
    if n == 0:
        return
    print(n)              # 🔹 happens immediately
    countdown(n - 1)

# Count up
# 1-2-3-4
def countup(n):
    if n == 0:
        return
    countup(n-1)
    print(n)

print(countup(5))



# Power 
#2^3 = 8 -> 2*2*2 = 8
def power(x, n):
    if n == 0:
        return 1
    #return power(x, n-1) * x
#print(power(2,3))

# sum of all digits
# 432 -> 4+3+2 = 9
def Sum(n):
    if n < 10:
        return n
    return Sum(n//10) + n%10

print("Вийшло ", Sum(432))

def revers(s):
    if len(s) <= 1:
        return s
    return revers(s[1:]) + s[0]
print("Маша навпаки - ", revers("Маша"))


# bin search , given sorted arr and target return its index or -1
def bin(arr, target, l=0, r=None):
    if r is None:
        r = len(arr) -1
    if l > r:
        return -1
    
    mid = (l+r)//2

    if arr[mid] == target:
        return mid
    
    if target < arr[mid]:
        return bin(arr, target, l, mid-1)
    return bin(arr, target, mid+1, r)


