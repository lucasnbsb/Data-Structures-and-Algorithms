class Solution:
    def merge(self, intervals) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            lastVal = output[-1]
            if intervals[i][0] <= lastVal[1]:
                output[-1] = [output[-1][0],max(lastVal[1][1], intervals[i][1])]
            else:
                output.append(intervals[i])
        return output