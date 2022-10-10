class Solution:
    def isValid(s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if(i in pairs): # if the character is a closing bracket check the top and check for empty
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else: # opening brackets can stack up to infinity
                stack.append(i)
        return True if not stack else False # stack must be empty in the end

    print(isValid('()[((()}}}}}))]{}'))
