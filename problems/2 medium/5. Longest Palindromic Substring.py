class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(s, left, right):
            maxLength = 0
            maxLengthString = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if maxLength < (right-left+1):
                    maxLength = (right-left+1)
                    maxLengthString = s[left:right+1]
                left -= 1
                right += 1
            return maxLengthString
        
        longestLength = ''
        for i in range(len(s)):
            #odd length
            longestOdd = check(s, i, i)
            #even length
            longestEven =  check(s, i, i+1)

            if len(longestLength) < len(longestOdd):
                longestLength = longestOdd
            if len(longestLength) < len(longestEven):
                longestLength = longestEven

        return longestLength

