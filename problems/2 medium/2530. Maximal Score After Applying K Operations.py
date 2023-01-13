import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        maxheap = []
        for n in nums:
            heapq.heappush(maxheap, -n)
        
        for i in range(k):
            n = -heapq.heappop(maxheap)
            score += n
            heapq.heappush(maxheap, -math.ceil(float(n/3)))
        return score