class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def cantFeed(n, k):  # n being the number of candies and k the number of children
            return sum(candy//n for candy in candies) < k

        if k > sum(candies):  # more children than candy
            return 0

        l, r = 1, max(candies)+1
        while l < r:
            mid = l + ((r-l) >> 1)
            if cantFeed(mid, k):
                r = mid
            else:
                l = mid+1
        return (l-1)
