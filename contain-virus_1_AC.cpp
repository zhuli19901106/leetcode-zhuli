// I thought for about ten minutes on the optimal segregation strategy.
// Then I found this is simply a simulation problem.
// From tough to tedious, shame.
#include <queue>
#include <vector>
using std::queue;
using std::vector;

static const int off[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

class Solution {
public:
    int containVirus(vector<vector<int>>& grid) {
		n = grid.size();
		m = grid[0].size();
		
		int i, j;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				g[i][j] = grid[i][j];
			}
		}
		
		int id, mid;
		int cnt, mcnt;
		int wc, mwc;
		int res = 0;
		while (true) {
			mid = 0;
			mcnt = 0;
			mwc = 0;
			
			id = -1;
			for (i = 0; i < n; ++i) {
				for (j = 0; j < m; ++j) {
					if (g[i][j] != 1) {
						continue;
					}
					flood(i, j, 1, id);
					countInfect(id, cnt, wc);
					if (cnt > mcnt) {
						mid = id;
						mcnt = cnt;
						mwc = wc;
					}
					--id;
				}
			}
			if (mid == 0 || mwc == 0) {
				// no more infection, or nothing left to infect.
				break;
			}
			
			buildWall(mid);
			res += mwc;
			
			for (i = 0; i < n; ++i) {
				for (j = 0; j < m; ++j) {
					if (g[i][j] < 0) {
						g[i][j] = 1;
					}
				}
			}
			
			spread();
		}
		
		return res;
    }
private:
	static const int MAXN = 50;
	int n, m;
	int g[MAXN + 5][MAXN + 5];
	
	inline bool inbound(int i, int j) {
		return i >= 0 && i <= n - 1 && j >= 0 && j <= m - 1;
	}
	
	/*
	// The internal implementation of queue is a linked list, which incurs larger constant overhead.
	void flood(int si, int sj, int v1, int v2) {
		queue<int> q;
		int i, j;
		int k;
		int i1, j1;
		int val;
		
		q.push(si * m + sj);
		while (!q.empty()) {
			val = q.front();
			q.pop();
			i = val / m;
			j = val % m;
			g[i][j] = v2;
			for (k = 0; k < 4; ++k) {
				i1 = i + off[k][0];
				j1 = j + off[k][1];
				if (inbound(i1, j1) && g[i1][j1] == v1) {
					q.push(i1 * m + j1);
				}
			}
		}
	}
	*/
	
	// smaller overhead, but susceptible to stack overflow
	void flood(int i, int j, int v1, int v2) {
		int k;
		int i1, j1;
		
		g[i][j] = v2;
		for (k = 0; k < 4; ++k) {
			i1 = i + off[k][0];
			j1 = j + off[k][1];
			if (inbound(i1, j1) && g[i1][j1] == v1) {
				flood(i1, j1, v1, v2);
			}
		}
	}
	
	void countInfect(int id, int &cnt, int &wc) {
		int i, j;
		int k;
		int i1, j1;
		int f;
		
		cnt = 0;
		wc = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (g[i][j] != 0) {
					continue;
				}
				f = 0;
				for (k = 0; k < 4; ++k) {
					i1 = i + off[k][0];
					j1 = j + off[k][1];
					if (inbound(i1, j1) && g[i1][j1] == id) {
						++wc;
						f = 1;
					}
				}
				cnt += f;
			}
		}
	}
	
	void buildWall(int id) {
		int i, j;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (g[i][j] == id) {
					flood(i, j, id, 2);
					return;
				}
			}
		}
	}
	
	void spread() {
		int i, j;
		int k;
		int i1, j1;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (g[i][j] != 0) {
					continue;
				}
				for (k = 0; k < 4; ++k) {
					i1 = i + off[k][0];
					j1 = j + off[k][1];
					if (inbound(i1, j1) && g[i1][j1] == 1) {
						g[i][j] = 3;
						break;
					}
				}
			}
		}
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (g[i][j] == 3) {
					g[i][j] = 1;
				}
			}
		}
	}
	
	void print() {
		int i, j;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				printf("%d ", g[i][j]);
			}
			printf("\n");
		}
		printf("\n");
	}
};
