# Programming question - Given reverse polish notation, 
# return the integer value of the expression aka "5,3,+,2,/" 
# would be 5 + 3 = 8 and then 8 / 2 = 4.
from collections import deque 

class PolishCalculator:
    def evaluate(exp: list[str]):
        stack = deque();
        for c in exp:
            if c.isnumeric():
                stack.append(int(c))
            else:
                if len(stack) >=2:
                    opperand2 = stack.pop()
                    opperand1 = stack.pop()
                else:
                    return 'Operacao mal formada'

                if c == '+':
                    stack.append(opperand1 + opperand2)
                elif c == '-':
                    stack.append(opperand1 - opperand2)
                elif c == '*':
                    stack.append(opperand1 * opperand2)
                elif c == '/':
                    if opperand2 == 0:
                        return 'Divisao por zero'
                    else:
                        stack.append(opperand1 / opperand2)
                else:
                    return 'Operador invalido '+c
        return stack.pop() if len(stack) == 1 else 'Operacao mal formada'
    print(evaluate(['5', '3', '*','2', '/']))    
