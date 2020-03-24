#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int la = A.size();
        int lb = B.size();
        vector<vector<int>> dp(la, vector<int>(lb, 0));
        
        int res = 0;
        int i, j;
        for (i = 0; i < la; ++i) {
            dp[i][0] = (A[i] == B[0] ? 1 : 0);
            res = max(res, dp[i][0]);
        }
        for (j = 0; j < lb; ++j) {
            dp[0][j] = (A[0] == B[j] ? 1: 0);
            res = max(res, dp[0][j]);
        }
        for (i = 1; i < la; ++i) {
            for (j = 1; j < lb; ++j) {
                dp[i][j] = (A[i] == B[j] ? dp[i - 1][j - 1] + 1 : 0);
                res = max(res, dp[i][j]);
            }
        }
        dp.clear();
        
        return res;
    }
};
