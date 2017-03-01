#include <utility>
#include <vector>
using std::pair;
using std::vector;

class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        vector<int> dj(n);
        int i;
        for (i = 0; i < n; ++i) {
            dj[i] = i;
        }
        
        int x, y;
        int rx, ry;
        int ne = edges.size();
        for (i = 0; i < ne; ++i) {
            x = edges[i].first;
            y = edges[i].second;
            rx = findRoot(dj, x);
            ry = findRoot(dj, y);
            if (rx == ry) {
                continue;
            }
            dj[rx] = ry;
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            if (findRoot(dj, i) == i) {
                ++res;
            }
        }
        dj.clear();
        return res;
    }
private:
    int findRoot(vector<int> &dj, int x) {
        int r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        int k = x;
        while (x != r) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
