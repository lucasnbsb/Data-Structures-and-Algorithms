class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        i = len(text1)
        j = len(text2)

        dp = [[0]*(j+1) for k in range(i+1)]
        for x in range(i-1, -1, -1):
            for y in range(j-1, -1, -1):
                if text1[x] == text2[y]:
                    dp[x][y] = 1 + dp[x+1][y+1]
                else:
                    dp[x][y] = max(dp[x+1][y], dp[x][y+1])
        return dp[0][0]