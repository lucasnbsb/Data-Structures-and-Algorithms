class Solution(object):
    def maximalSquare(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        maxSide = 0
        
        # first row
        for r in range(ROWS):
            if matrix[r][0] == '1':
                maxSide = 1
        # first column
        for c in range(COLS):
            if matrix[0][c] == '1':
                maxSide = 1

        # miolo
        for r in range(1, ROWS):
            for c in range(1,COLS):
                if matrix[r][c] == '1':
                    matrix[r][c] = str(1 + min(int(matrix[r-1][c-1]), int(matrix[r-1][c]), int(matrix[r][c-1])))
                    maxSide = max(maxSide, int(matrix[r][c]))

        return maxSide*maxSide