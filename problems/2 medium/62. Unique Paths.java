class Solution {
    public int uniquePaths(int m, int n) {
        // start from the end and run back to the begining.
    	// last column and last row are always filled with ones.
    	
    	int[][]dp = new int[m][n];
    	
    	// last row
    	for (int i = 0; i < n; i++) {
			dp[m-1][i] = 1;
		}
    	
    	// last column
    	for (int j = 0; j < n; j++) {
			dp[j][n-1] = 1;
		}
		
    	for (int i = m-2; i >= 0; i--) {
			for(int j = n-2; j >= 0; j--) {
				dp[i][j] = dp[i+1][j] + dp[i][j+1];
			}
		}
    	return dp[0][0];
    }
}