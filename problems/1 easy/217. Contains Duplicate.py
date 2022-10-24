class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num not in vals:
                vals[num] = 0
            else:
                return True
        return False