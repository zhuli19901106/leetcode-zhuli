// O(nk) time and O(k) space DP
#include <algorithm>
#include <climits>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        auto &c = costs;
        int n = c.size();
        if (n == 0) {
            return 0;
        }
        int k = c[0].size();
        
        vector<vector<int>> dp(2, vector<int>(k));
        vector<int> vm(k);
        int i, j;
        
        for (i = 0; i < k; ++i) {
            dp[0][i] = c[0][i];
        }
        
        int f = 1;
        int nf = !f;
        for (i = 1; i < n; ++i) {
            minExceptSelf(dp[nf], vm);
            for (j = 0; j < k; ++j) {
                dp[f][j] = vm[j] + c[i][j];
            }
            f = !f;
            nf = !f;
        }
        
        int res = INT_MAX;
        for (i = 0; i < k; ++i) {
            res = min(res, dp[nf][i]);
        }
        dp.clear();
        vm.clear();
        
        return res;
    }
private:
    void minExceptSelf(vector<int> &v, vector<int> &m) {
        int n = v.size();
        int i;
        for (i = 0; i <= n - 1; ++i) {
            m[i] = INT_MAX;
        }
        
        int min_val = INT_MAX;
        for (i = 0; i <= n - 1; ++i) {
            m[i] = min(m[i], min_val);
            min_val = min(min_val, v[i]);
        }
        min_val = INT_MAX;
        for (i = n - 1; i >= 0; --i) {
            m[i] = min(m[i], min_val);
            min_val = min(min_val, v[i]);
        }
    }
};
