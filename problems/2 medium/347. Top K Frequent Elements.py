import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if len(nums)==1: return nums

        counter = collections.defaultdict(int)
        maxHeap = []
        for n in nums:
            counter[n] += 1
        
        for key in counter.keys():
            heapq.heappush(maxHeap, [-counter[key], key])

        output = []
        for i in range(k):
            value, key = heapq.heappop(maxHeap)
            output.append(key)

        return output