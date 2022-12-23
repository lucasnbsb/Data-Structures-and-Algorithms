from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = set(('*', '-', '+', '/'))
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if len(stack) >= 2 :
                    op2 = stack.pop()
                    op1 = stack.pop()
                    if t == '+':
                        stack.append(op1 + op2)
                    elif t == '-':
                        stack.append(op1 - op2)
                    elif t == '*':
                        stack.append(op1 * op2)
                    elif t == '/':
                        stack.append(int(float(op1)/op2))
                    else:
                        return -1 
                else:
                    return -2
        return stack.pop()
