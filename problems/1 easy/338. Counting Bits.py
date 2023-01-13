class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            cur = 0
            while i:
                cur += i&1
                i = i>>1
            output.append(cur)
        return output