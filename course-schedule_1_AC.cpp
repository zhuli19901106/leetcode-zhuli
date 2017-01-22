// Topological sort using BFS.
#include <queue>
#include <vector>
using std::queue;
using std::vector;

class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        int nv = numCourses;
        vector<vector<int>> g(nv);
        vector<int> ind(nv, 0);
        auto &e = prerequisites;
        queue<int> q;
        int x, y;
        int ne = e.size();
        
        int i;
        for (i = 0; i < ne; ++i) {
            x = e[i].second;
            y = e[i].first;
            g[x].push_back(y);
            ++ind[y];
        }
        
        for (i = 0; i < nv; ++i) {
            if (ind[i] == 0) {
                q.push(i);
            }
        }
        
        int ec = ne;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            while (g[x].size() > 0) {
                y = g[x].back();
                g[x].pop_back();
                --ind[y];
                --ec;
                if (ind[y] == 0) {
                    q.push(y);
                }
            }
        }
        return ec == 0;
    }
};
