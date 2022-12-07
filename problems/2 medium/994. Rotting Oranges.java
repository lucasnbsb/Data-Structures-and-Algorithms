import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Iterator;

class Solution {
	public int orangesRotting(int[][] grid) {
		int ROWS = grid.length;
		int COLS = grid[0].length;

		Deque<int[]> queue = new ArrayDeque<int[]>();
		int[][] rotten = new int[ROWS][COLS];
		int numFresh = 0;

		for (int r = 0; r < ROWS; r++) {
			for (int c = 0; c < COLS; c++) {
				if (grid[r][c] == 1) {
					numFresh++;
				} else if (grid[r][c] == 2) {
					queue.add(new int[] { r, c });
				}
			}
		}

		int time = 0;
		while (!queue.isEmpty() && numFresh > 0) {
			time++;
			int qsize = queue.size();
			for (int i = 0; i < qsize; i++) {
				int[] curr = queue.poll();
				int r = curr[0];
				int c = curr[1];
				int[][] directions = { { r + 1, c }, { r - 1, c }, { r, c + 1 }, { r, c - 1 } };
				for (int[] dir : directions) {
					int dr = dir[0];
					int dc = dir[1];
					if ((Math.min(dr, dc) >= 0) && (dr < ROWS) && (dc < COLS) && (grid[dr][dc] == 1)) {
						grid[dr][dc] = 2;
						queue.add(dir);
						numFresh -= 1;
					}
				}
			}
		}
		return numFresh == 0? time: -1;
	}
}