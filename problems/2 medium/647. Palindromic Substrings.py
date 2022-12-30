class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(s, l, r):
            numSubs = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numSubs += 1
                l -= 1
                r += 1
            return numSubs

        totalSubstrings = 0
        #odd lengths:
        for i in range(len(s)):
            # odd lengths
            totalSubstrings += check(s, i, i)
            # even lengths
            totalSubstrings += check(s, i, i+1)
        return totalSubstrings