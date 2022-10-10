
class Solution:
    def guessNumber(self, n: int) -> int:
        l,h  = 1, n
        mid = (l+h)>>1
        
        while(res := guess(mid)) != 0:
            if(res == 1):
                l = mid+1
            else:
                h = mid-1
            mid = (l+h)>>1
        return mid