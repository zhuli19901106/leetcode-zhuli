#include <vector>
using std::vector;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        if (n < 2) {
            return n;
        }
        
        vector<int> dj(n);
        int x;
        for (x = 0; x < n; ++x) {
            dj[x] = x;
        }
        
        int y;
        int rx, ry;
        for (x = 0; x < n; ++x) {
            for (y = x + 1; y < n; ++y) {
                if (M[x][y] == 0) {
                    continue;
                }
                rx = findRoot(dj, x);
                ry = findRoot(dj, y);
                if (rx == ry) {
                    continue;
                }
                dj[rx] = ry;
            }
        }
        
        int cnt = 0;
        for (x = 0; x < n; ++x) {
            if (findRoot(dj, x) == x) {
                ++cnt;
            }
        }
        dj.clear();
        
        return cnt;
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
