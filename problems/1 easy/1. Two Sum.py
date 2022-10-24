class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash:
                return [hash[dif], i]
            hash[nums[i]] = i
        