"""
Write a function that takes in two non-empty arrays, finds the pair of numbers(one from each array)
whose absolute difference is closest to zero. Assume that there will be only one pair of numbers with smallest difference
Sample inputs - Expected outputs
Example
Input
A = [1, 3, 15, 11, 2]
B = [23, 127, 235, 19, 8]
Output
[11, 8]



"""
"""
Time: N*M
Space: 1, because we always will have just 2 vals in the res
"""
def smallest_abs_diff(A, B):
    """output: elemnt from A and elemnt from B stored in a list"""
    res = []
    diff = float('inf')
    for n in range(len(A)):
        for m in range(len(B)):
            cur_diff = abs(A[n] - B[m])  

            if cur_diff < diff:
                res = [A[n], B[m]]
                diff = cur_diff
    
    return res

"""
Time: O(N log N + M log N)
Space: O(1), constant number of variables used
"""
def smallest_abs_diff(A, B):
    A.sort()
    B.sort()
    smallest = float('inf')
    res = []
    p1 = 0
    p2 = 0

    while p1 < len(A) and p2 < len(B):
        first = A[p1]
        second = B[p2]
        cur_diff = abs(first - second)

        if cur_diff < smallest:
            smallest = cur_diff
            res = first, second

        if first > second:
            p2 +=1
        elif first < second:
            p1 +=1
        else:
            return [first, second]