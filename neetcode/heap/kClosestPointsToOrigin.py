'''
K Closest Points to Origin
Solved 
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100

'''


import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each coordinate do a func and store the diff in dict: coordinates : diff
        # and add this diif to heap to heapify then 
        # do heap on each oordinete 
        # then heappop until 
        res = []
        heap = []
        dic = {} #coord : diff
        X, Y = 0, 0
        for coordinate in points:
            x, y = coordinate[0], coordinate[1]
            diff = math.sqrt((x - X)**2 + (y - Y)**2)
            dic[tuple(coordinate)] = diff

        for val in dic.values():
            heapq.heappush(heap, val)

        while heap and len(res) < k:
            popped = heapq.heappop(heap)
            for coordinate, diff in dic.items():
                if dic[tuple(coordinate)] == popped:
                    res.append(list(coordinate))

        return res
    
# time: nlogn
# space: N

# Optimized no dict
# bc in heap soerting is done to the first elem in the list
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        
        for coordinate in points:
            x, y = coordinate
            diff = (x**2) + (y**2)
            heap.append((diff, coordinate))

        heapq.heapify(heap)

        while k > 0:
            diff, coord = heapq.heappop(heap)
            res.append(coord)
            k -=1
        return res


# O(n + k log n) time
# space N