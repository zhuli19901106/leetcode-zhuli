#include <algorithm>
#include <functional>
#include <vector>
using std::function;
using std::max;
using std::min;

typedef bool (*FunComp)(const int &, const int &);

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        FunComp lessThan = [](const int &x, const int &y){return x < y;};
        
        int na = arrays.size();
        int n;
        int i, j;
        int min_val, max_val;
        
        vector<int> vmin(na), vmax(na);
        for (i = 0; i < na; ++i) {
            n = arrays[i].size();
            vmin[i] = vmax[i] = arrays[i][0];
            for (j = 1; j < n; ++j) {
                vmin[i] = min(vmin[i], arrays[i][j]);
                vmax[i] = max(vmax[i], arrays[i][j]);
            }
        }
        
        vector<int> vmin1;
        exceptSelf(vmin, vmin1, lessThan);
        
        int res = 0;
        for (i = 0; i < na; ++i) {
            res = max(res, vmax[i] - vmin1[i]);
        }
        
        return res;
    }
private:
    void exceptSelf(vector<int> &vin, vector<int> &vout, FunComp &cmp) {
        int n = vin.size();
        if (n < 2) {
            vout = vin;
            return;
        }
        
        vector<int> v1(n), v2(n);
        int i;
        
        v1[0] = vin[0];
        for (i = 1; i <= n - 1; ++i) {
            v1[i] = (cmp(vin[i], v1[i - 1]) ? vin[i] : v1[i - 1]);
        }
        v2[n - 1] = vin[n - 1];
        for (i = n - 2; i >= 0; --i) {
            v2[i] = (cmp(vin[i], v2[i + 1]) ? vin[i] : v2[i + 1]);
        }
        
        vout.resize(n);
        vout[0] = v2[1];
        for (i = 1; i < n - 1; ++i) {
            vout[i] = (cmp(v1[i - 1], v2[i + 1]) ? v1[i - 1] : v2[i + 1]);
        }
        vout[n - 1] = v1[n - 2];
    }
};
