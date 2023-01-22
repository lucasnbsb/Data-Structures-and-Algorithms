class Solution:
    def alternateDigitSum(self, n: int) -> int:
        strn = str(n)
        sign = 1
        out = 0
        for c in strn:
            out += sign * int(c)
            sign *= -1
        return out
                