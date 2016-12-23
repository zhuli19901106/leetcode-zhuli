// Careful with the formulae
#include <alogorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    Solution() {
        dp.push_back(0);
        dp.push_back(1);
        dp.push_back(1);
    }
    
    int integerBreak(int n) {
        while (dp.size() <= n) {
            calcNext();
        }
        return dp[n];
    }
private:
    vector<int> dp;
    
    void calcNext() {
        int n = dp.size();
        dp.push_back(dp[n - 1]);
        int i;
        for (i = 2; i < n; ++i) {
            dp[n] = max(dp[n], i * max(n - i,dp[n - i]));
        }
    }
};
