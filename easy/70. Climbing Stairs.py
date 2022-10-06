# remember the tree representation. this is the lowest level of dp out there
class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 1, 1
        for c in range(n - 1):
            temp = i
            i = i+j
            j = temp
        return i
