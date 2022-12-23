import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # total time nLog(n)
        numsMap = {}
        # O(n)
        for n in nums: 
            numsMap[n] = n
        
        curSeqLength = 0
        maxSeq = 0
        for n in nums:
            if n-1 not in numsMap:
                curSubsequence = n
                while curSubsequence in numsMap:
                    curSeqLength += 1
                    maxSeq = max(maxSeq, curSeqLength)
                    curSubsequence += 1
            curSeqLength = 0
        
        return maxSeq

            
