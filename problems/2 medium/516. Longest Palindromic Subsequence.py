class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)        
        dp = [[0]* size for i in range(size)]
        for l in range(size-1, -1, -1):
            for r in range(l, size):
                if l == r: dp[l][r] = 1
                else:
                    if s[l] == s[r]: dp[l][r] = 2 + dp[l+1][r-1]
                    else: dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return dp[0][-1]