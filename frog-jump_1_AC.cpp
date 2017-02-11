// BFS
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::queue;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    bool canCross(vector<int>& stones) {
        auto &a = stones;
        int n = a.size();
        int i, j, k;
        
        // Remove consecutive duplicates
        i = 0;
        k = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && a[i] == a[j]) {
                ++j;
            }
            a[k++] = a[i];
            i = j;
        }
        n = k;
        a.resize(n);
        
        vector<unordered_set<int>> v(n);
        vector<bool> b(n, false);
        unordered_map<int, int> um;
        
        for (i = 0; i < n; ++i) {
            um[a[i]] = i;
        }
        
        queue<pair<int, int>> q;
        pair<int, int> p;
        int x, y;
        
        b[0] = true;
        q.push(make_pair(0, 1));
        while (!b[n - 1] && !q.empty()) {
            p = q.front();
            q.pop();
            x = p.first;
            y = p.second;
            if (um.find(x + y) == um.end()) {
                // Into the river
                continue;
            }
            
            i = um[x + y];
            if (v[i].find(y) != v[i].end()) {
                // Already marked
                continue;
            }
            
            // Reachable
            b[i] = true;
            v[i].insert(y);
            
            if (y > 1) {
                q.push(make_pair(x + y, y - 1));
            }
            q.push(make_pair(x + y, y));
            q.push(make_pair(x + y, y + 1));
        }
        
        bool res = b[n - 1];
        while (!q.empty()) {
            q.pop();
        }
        v.clear();
        b.clear();
        um.clear();
        
        return res;
    }
};
