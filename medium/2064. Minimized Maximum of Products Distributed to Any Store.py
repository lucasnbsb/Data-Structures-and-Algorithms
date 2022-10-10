class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(k):
            return sum(-(-quantity // k) for quantity in quantities) <= n

        l, r = 1, max(quantities)
        while l < r:
            mid = l + ((r-l) >> 1)
            if canDistribute(mid):
                r = mid
            else:
                l = mid+1
        return l
