import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        # 1: 1
        # 2: 2
        # 3: 3
        heap = []
        for num, count in dic.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]

        '''
time
Each heappush → O(log k)
Each heappop (if needed) → O(log k)
Total → O(n log k)
Building the result list from the heap → O(k)
Final Time: O(n log k)

space
Frequency dictionary → O(n) (storing counts for each unique number).
Heap → O(k) (we keep at most k elements in the heap).
Result list → O(k)
Final Space: O(n + k)
        '''
