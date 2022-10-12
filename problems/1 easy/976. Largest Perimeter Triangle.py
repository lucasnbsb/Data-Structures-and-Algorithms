class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def canFormTriangle(nums):
            return ((nums[0]+nums[1])>nums[2] and (nums[2]+nums[1])>nums[0] and (nums[0]+nums[2])>nums[1])
        
        
        for i in range(len(nums)-1, 1, -1):
            if canFormTriangle([nums[i], nums[i-1], nums[i-2]]):
                return nums[i]+nums[i-1]+nums[i-2]
        return 0