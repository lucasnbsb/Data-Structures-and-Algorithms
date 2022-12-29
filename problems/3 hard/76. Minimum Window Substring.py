class Solution:
    def mapOneContainsMapTwo(self,mapOne, mapTwo):
        for k in mapOne:
            if k not in mapTwo or mapOne[k] > mapTwo[k]: 
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counterT = collections.defaultdict(int)
        for c in t:
            counterT[c] += 1

        left = 0
        minWindow = s+' '
        counterWindow = collections.defaultdict(int)
        for right, c in enumerate(s):
            if c in counterT:
                counterWindow[c] += 1
            
            while self.mapOneContainsMapTwo(counterT, counterWindow): 
                if (right-left+1 < len(minWindow)):
                    minWindow = s[left:right+1]
                
                if s[left] in counterWindow:
                    counterWindow[s[left]] -= 1
                    if counterWindow[s[left]] <= 0:
                        del counterWindow[s[left]]
                left += 1

        return '' if minWindow == s+' ' else minWindow
