// DP with memorization
// Always watch out for overflow.
#include <algorithm>
#include <climits>
#include <unordered_map>
using std::min;
using std::unordered_map;

class Solution {
public:
    Solution() {
        dp[1] = 0;
        dp[INT_MAX] = 32;
    }
    
    int integerReplacement(int n) {
        if (dp.find(n) == dp.end()) {
            if (n & 1) {
                dp[n] = min(integerReplacement(n + 1), integerReplacement(n - 1)) + 1;
            } else {
                dp[n] = integerReplacement(n >> 1) + 1;
            }
        }
        return dp[n];
    }
    
    ~Solution() {
        dp.clear();
    }
private:
    unordered_map<int, int> dp;
};
