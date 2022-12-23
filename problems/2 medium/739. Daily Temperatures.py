class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #last position is always a 0, all positions not found in the queue are also 0
        output = [0]*len(temperatures)
        tempStack = deque()
        
        #tempStack = stack([temp, index])
        for i, t in enumerate(temperatures):
            while tempStack and t > tempStack[-1][0]:
                output[tempStack[-1][1]] = i - tempStack[-1][1]
                tempStack.pop()
            
            if not tempStack or t <= tempStack[-1][0]:
                tempStack.append([t, i])

        return output