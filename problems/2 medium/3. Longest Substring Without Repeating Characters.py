class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        prev = set()
        maxSize = 0
        for r in range(len(s)):
            while s[r] in prev:
                prev.remove(s[left])
                left += 1
            prev.add(s[r])
            maxSize = max(maxSize, r-left+1)
        return maxSize