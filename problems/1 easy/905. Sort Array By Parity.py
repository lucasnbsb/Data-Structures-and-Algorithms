class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for num in nums:
            if num%2:
                odds.append(num)
            else:
                evens.append(num)
        return evens+odds