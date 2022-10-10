class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(k):
            return sum(-(-pile//k) for pile in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l)//2
            if canEat(mid):
                r = mid
            else:
                l = mid+1
        return l
