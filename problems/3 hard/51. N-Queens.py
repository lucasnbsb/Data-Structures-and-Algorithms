class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        def dfs(rows, _sum, _diff):
            p = len(rows)
            if p == n:
                output.append(rows)
                return
            
            for q in range(n):
                currDiff = p-q
                currSum = p+q
                if q not in rows and currDiff not in _diff and currSum not in _sum:
                    dfs(rows+[q], _sum+[currSum], _diff+[currDiff])
        dfs([], [], [])

        finalOutput = []
        for solution in output:
            partialOutput = []
            for col in solution:
                partialOutput = partialOutput + ["." * col +  "Q" + "."*(n-col-1)]
            finalOutput.append(partialOutput)
        return finalOutput