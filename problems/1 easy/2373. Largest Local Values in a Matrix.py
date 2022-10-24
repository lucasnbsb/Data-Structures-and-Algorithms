class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output = [[] for i in range(len(grid)-2)]
        print(output)
        for i in range(0, len(grid) -2):
            for j in range(0, len(grid[0])-2):
                n,m = i+1, j+1
                output[i].append(max(grid[n+1][m-1], grid[n+1][m], grid[n+1][m+1], grid[n][m-1], grid[n][m], grid[n][m+1], grid[n-1][m-1], grid[n-1][m], grid[n-1][m+1]))
        return output