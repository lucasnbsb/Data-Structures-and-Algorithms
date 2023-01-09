class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output ^= i
        return output