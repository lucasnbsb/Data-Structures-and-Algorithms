class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        intS = int(s)
        intTarget = int(target)
        
        if intS == intTarget: return True
        
        if intS > 0 and intTarget == 0: return False
        
        if intS == 0 and intTarget > 0: return False
        
        return True