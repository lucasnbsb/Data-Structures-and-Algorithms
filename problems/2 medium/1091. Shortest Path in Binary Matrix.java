import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Iterator;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int[][] visited = new int[ROWS][COLS];
        Deque<int[]> queue = new ArrayDeque<>();
        if(grid[0][0] == 1){
            return -1;
        }

        queue.add(new int[2]);
        visited[0][0] = 1;
        
        int length = 1;
        while(!queue.isEmpty()){
        	int qlength = queue.size();
        	for (int i = 0; i < qlength; i++) {
        		int[]curr = queue.poll(); //popleft
				int r = curr[0];
				int c = curr[1];
                if(r == ROWS-1 && c == COLS-1){
                    return length;
                }
				int[][]vizinhos = {{r+1,c}, {r-1, c}, {r,c+1}, {r,c-1}, {r-1,c-1}, {r+1,c+1}, {r-1,c+1}, {r+1,c-1}};
				for (int j = 0; j < 8; j++) {
					int currR = vizinhos[j][0];
					int currC = vizinhos[j][1];
					
					if (
						(Math.min(currR, currC) < 0) || 
						(currR == ROWS) ||
						(currC == COLS) ||
						(visited[currR][currC] == 1) ||
						(grid[currR][currC] == 1)
					) {
						continue;
					}
					queue.add(vizinhos[j]);
					visited[currR][currC] = 1;
				}
			}
        	length++;
        }
        return -1;
    }
}