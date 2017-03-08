// Make sure you calculate the cumulated sum in the right way.
#include <algorithm>
#include <climits>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        auto &a = grid;
        int n = a.size();
        int m = (n > 0 ? a[0].size() : 0);
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<int> ci(n, 0), cj(m, 0);
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == 1) {
                    ++ci[i];
                    ++cj[j];
                }
            }
        }
        
        vector<int> vl(m, 0), vr(m, 0), vu(n, 0), vd(n, 0);
        int sum;
        
        sum = cj[0];
        for (j = 1; j <= m - 1; ++j) {
            vl[j] = vl[j - 1] + sum;
            sum += cj[j];
        }
        sum = cj[m - 1];
        for (j = m - 2; j >= 0; --j) {
            vr[j] = vr[j + 1] + sum;
            sum += cj[j];
        }
        sum = ci[0];
        for (i = 1; i <= n - 1; ++i) {
            vu[i] = vu[i - 1] + sum;
            sum += ci[i];
        }
        sum = ci[n - 1];
        for (i = n - 2; i >= 0; --i) {
            vd[i] = vd[i + 1] + sum;
            sum += ci[i];
        }
        
        int res = INT_MAX;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                sum = vl[j] + vr[j] + vu[i] + vd[i];
                res = min(res, sum);
            }
        }
        
        ci.clear();
        cj.clear();
        
        vl.clear();
        vr.clear();
        vu.clear();
        vd.clear();
        
        return res;
    }
};
