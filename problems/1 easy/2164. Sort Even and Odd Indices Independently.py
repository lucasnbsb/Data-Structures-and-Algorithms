class Solution:
    #nums is small enough
    def bucketSort(self, nums):
        buckets = [0]*101
        res = []
        for num in nums:
            buckets[num] += 1
            
        for i in range(len(buckets)):
            for j in range(buckets[i]):
                res.append(i)
        return res
    
    
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        
        for i in range(len(nums)):
            if i%2:
                odds.append(nums[i])
            else:
                evens.append(nums[i])
                
        odds = self.bucketSort(odds)
        evens = self.bucketSort(evens)[::-1]
        
        res = []
        i = j = 0
        for i in range(len(nums)):
            if i%2:
                res.append(odds.pop())
            else:
                res.append(evens.pop())
        return res
