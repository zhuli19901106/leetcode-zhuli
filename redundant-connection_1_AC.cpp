#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        unordered_map<int, int> dj;
        int x, y;
        int rx, ry;
        for (auto &v: edges) {
            x = v[0];
            y = v[1];
            rx = findRoot(dj, x);
            ry = findRoot(dj, y);
            if (rx == ry) {
                return v;
            } else {
                dj[rx] = ry;
            }
        }
        return vector<int>();
    }
private:
    int findRoot(unordered_map<int, int> &dj, int x) {
        if (dj.find(x) == dj.end()) {
            dj[x] = x;
            return x;
        }
        
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
