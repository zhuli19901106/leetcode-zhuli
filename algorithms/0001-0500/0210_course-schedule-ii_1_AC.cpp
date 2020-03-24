// Watch for duplicate edges.
#include <queue>
#include <unordered_map>
#include <unordered_set>
using std::queue;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        int nv = numCourses;
        auto &e = prerequisites;
        int ne = e.size();
        unordered_map<int, unordered_set<int>> g;
        vector<int> ind(nv, 0);
        int x, y;
        int i;
        for (i = 0; i < ne; ++i) {
            x = e[i].second;
            y = e[i].first;
            if (g[x].find(y) != g[x].end()) {
                continue;
            }
            g[x].insert(y);
            ++ind[y];
        }
        
        queue<int> q;
        for (i = 0; i < nv; ++i) {
            if (ind[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> res;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            res.push_back(x);
            for (auto it = g[x].begin(); it != g[x].end(); ++it) {
                y = *it;
                --ind[y];
                if (ind[y] == 0) {
                    q.push(y);
                }
            }
            g[x].clear();
        }
        g.clear();
        ind.clear();
        if (res.size() < nv) {
            res.clear();
        }
        return res;
    }
};
