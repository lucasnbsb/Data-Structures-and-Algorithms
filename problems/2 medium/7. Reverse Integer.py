class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        def isInRange(n):
            return -2**31 <= n <= (2**31)-1
        
        isneg = x < 0
        x = abs(x)
        
        while(x > 0):
            mod = x % 10
            x = x // 10
            output+=mod
            output=output*10
        output = output//10
        
        if isneg:
            output = output *-1
        
        if isInRange(output):
            return output
        else:
            return 0