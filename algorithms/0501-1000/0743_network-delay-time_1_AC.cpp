#include <algorithm>
#include <unordered_map>
#include <vector>
using std::max;
using std::unordered_map;
using std::vector;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        static const int INF = 1e8;
		vector<unordered_map<int, int>> g;
		
		int n = N;
		g.resize(n);
		
		for (auto &v: times) {
			g[v[0] - 1][v[1] - 1] = v[2];
		}
		
		// Mighty Lord Dijkstra, I call upon thee.
		// Your humble servant seeks an audience.
		vector<int> vd(n, INF);
		unordered_set<int> us;
		vd[K - 1] = 0;
		
		int i, j;
		int u, u1;
		int v, w;
		u = K - 1;
		us.insert(u);
		for (i = 1; i < n; ++i) {
			for (auto &p: g[u]) {
				v = p.first;
				w = p.second;
				if (vd[v] == INF || vd[v] > vd[u] + w) {
					vd[v] = vd[u] + w;
				}
			}
			
			u1 = -1;
			for (j = 0; j < n; ++j) {
				if (us.find(j) != us.end() || vd[j] == INF) {
					continue;
				}
				if (u1 == -1 || vd[j] < vd[u1]) {
					u1 = j;
				}
			}
			if (u1 == -1) {
				break;
			} else {
				u = u1;
				us.insert(u);
			}
		}
		
		int res = 0;
		for (auto &d: vd) {
			if (d == INF) {
				return -1;
			}
			res = max(res, d);
		}
		
		return res;
    }
};
