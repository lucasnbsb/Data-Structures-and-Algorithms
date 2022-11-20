class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keys = {
            '2':['a', 'b', 'c'],
            '3':['d','e','f'],    
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r', 's'],
            '8':['t','u','v'],
            '9':['w','x','y', 'z'],
        }
        
        output = []
        currentString = deque();

        def dfs(remainingDigits):
            if len(remainingDigits) == 0:
                output.append(''.join(currentString))
                return None

            letters = keys[remainingDigits[0]]
            for l in letters:
                currentString.append(l)
                dfs(remainingDigits[1:])
                currentString.pop()
            return None

        dfs(digits)
        return output
            

            
