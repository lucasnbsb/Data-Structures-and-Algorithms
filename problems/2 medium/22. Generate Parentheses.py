class Solution:  
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []        
        def backtrack(nopen, nclosed):
            if nopen == n and nclosed == n:
                res.append(''.join(stack))
                return
            
            if nopen < n:
                stack.append('(')
                backtrack(nopen+1, nclosed)
                stack.pop()
            
            if nopen > nclosed:
                stack.append(')')
                backtrack(nopen, nclosed+1)
                stack.pop()
            

        backtrack(0,0)
        return res