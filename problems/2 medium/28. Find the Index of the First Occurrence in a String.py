class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        needlehash = hash(needle)
        for i in range(h-n+1):
            if hash(haystack[i:i+n]) == needlehash:
                return i
        return -1