
class DSU{
	int [] parent, rank;
	int nComponents = 0;
			
	public DSU(int n) {
		nComponents = n;
		parent = new int[n];
		rank = new int[n];
		
		for (int i = 0; i < n; i++) {
			parent[i] = i;
			rank[i] = 1;
		}
	}
	
	public int find(int x) {
		if(parent[x] != x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}
	
	public void union(int x, int y) {
		int rx = this.find(x);
		int ry = this.find(y);
		
		if(rx == ry) {
			return;
		}
		
		if(rank[ry] > rank[rx]) {
			parent[rx] = ry;
			rank[ry] += rank[rx];
		}else {
			parent[ry] = rx;
			rank[rx] += rank[ry];
		}
		
		nComponents--;
	}
	
}


class Solution {
    public int findCircleNum(int[][] isConnected) {
    	int n = isConnected.length;
        DSU dsu = new DSU(n);
        for (int i = 0; i < n; i++) {
        	for (int j = i; j < n; j++) {
            	if(isConnected[i][j] == 1) {
            		dsu.union(i, j);
            	}
    		}
		}
        return dsu.nComponents;
    }
}