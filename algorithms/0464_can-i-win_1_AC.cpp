#include <vector>
using std::vector;

class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        int n = maxChoosableInteger;
        int s = desiredTotal;
        if (n >= s) {
            return true;
        }
        if ((1 + n) * n / 2 < s) {
            return false;
        }
        
        // 1 for win, -1 for lose, 0 for unknown
        vector<int> dp(1 << n, 0);
        bool res = search(0, n, s, dp);
        dp.clear();
        
        return res;
    }
private:
    bool search(int mask, int n, int s, vector<int> &dp) {
        if (dp[mask] != 0) {
            return dp[mask] == 1;
        }
        int i;
        int i2;
        for (i = n; i > 0; --i) {
            i2 = (1 << i - 1);
            if ((mask & i2) != 0) {
                // Already used
                continue;
            }
            // 1 lose -> win
            // all win -> lose
            if (i >= s || !search(mask | i2, n, s - i, dp)) {
                dp[mask] = 1;
                return true;
            }
        }
        dp[mask] = -1;
        return false;
    }
};
