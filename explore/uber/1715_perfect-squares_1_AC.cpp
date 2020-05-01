#include <algorithm>
#include <climits>
#include <cmath>
#include <vector>
using std::min;
using std::sqrt;
using std::vector;

class Solution {
public:
    Solution() {
        dp.push_back(0);
    }
    
    int numSquares(int n) {
        while (dp.size() <= n) {
            calcNext();
        }
        return dp[n];
    }
    
    ~Solution() {
        dp.clear();
    }
private:
    vector<int> dp;
    
    void calcNext() {
        int n = dp.size();
        int i = sqrt(n);
        dp.push_back(INT_MAX);
        while (i > 0) {
            dp[n] = min(dp[n], dp[n - i * i] + 1);
            --i;
        }
    }
};
