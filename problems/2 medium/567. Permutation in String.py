class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n+m)
        # counters for the occurences 
        countS1 = collections.defaultdict(int)
        countS2 = collections.defaultdict(int)
        for s in s1: 
            countS1[s]+= 1
        size = len(s1)
        left = 0
        for right, s in enumerate(s2):
            if right < size:
                countS2[s] += 1
            else:
                countS2[s] += 1
                countS2[s2[left]] -= 1
                if countS2[s2[left]] == 0:
                    del countS2[s2[left]]
                left += 1
            if countS1 == countS2: return True
        return False