class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        sums = [0]
        for i in range(1,len(nums)):
            sum += nums[i-1]
            sums.append(sum)
        for i in range(0, len(nums)):
            if sums[i]*2 + nums[i] == sums[-1]+ nums[-1]:
                return i
        return -1