class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums & 1: return False
        capacity = sumNums//2

        sizeNums = len(nums)
        dp = [0] * (capacity + 1)
        
        # first line
        for c in range(capacity+1):
            if nums[0] <= c:
                dp[c] = nums[0]
                if dp[c] == capacity: return True

        for i in range(1, sizeNums):
            curRow = [0] * (capacity + 1)
            for c in range(1, (capacity + 1)):
                skip = dp[c]
                include = 0
                if c-nums[i]>=0:
                    include = nums[i] + dp[c-nums[i]]
                curRow[c] = max(include, skip)
                if curRow[c] == capacity: return True
            dp = curRow
        return False