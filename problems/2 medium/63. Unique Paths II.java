class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
    	int n = obstacleGrid[0].length;
    	
    	
    	int[][]dp = new int[m][n];
    	
    	// end position
    	if(obstacleGrid[m-1][n-1] == 1) {
    		return 0;
    	}else {
    		dp[m-1][n-1] = 1;
    	}
    	
    	// last row
    	for (int i = n-2; i >= 0; i--) {
    		dp[m-1][i] = obstacleGrid[m-1][i] == 1 ? 0:dp[m-1][i+1];
		}
    	
    	// last column
    	for (int j = m-2; j >= 0  ; j--) {
			dp[j][n-1] = obstacleGrid[j][n-1] == 1? 0:dp[j+1][n-1];
		}
		
    	for (int i = m-2; i >= 0; i--) {
			for(int j = n-2; j >= 0; j--) {
				dp[i][j] = obstacleGrid[i][j] == 1? 0: dp[i+1][j] + dp[i][j+1];
			}
		}
    	return dp[0][0];
    }
}