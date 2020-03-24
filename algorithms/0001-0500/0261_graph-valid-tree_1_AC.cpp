#include <utility>
#include <vector>
using std::pair;
using std::vector;

class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        if (n == 0) {
            return edges.size() == 0;
        }
        
        int ne = edges.size();
        if (ne != n - 1) {
            return false;
        }
        
        vector<int> dj(n);
        int i;
        for (i = 0; i < n; ++i) {
            dj[i] = i;
        }
        
        int x, y;
        int rx, ry;
        for (i = 0; i < ne; ++i) {
            x = edges[i].first;
            y = edges[i].second;
            rx = findRoot(dj, x);
            ry = findRoot(dj, y);
            if (rx == ry) {
                break;
            }
            dj[rx] = ry;
        }
        dj.clear();
        
        return i == ne;
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
