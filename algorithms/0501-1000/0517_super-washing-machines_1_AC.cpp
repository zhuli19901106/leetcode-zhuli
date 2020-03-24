// Solution by @Xianming.Chen
// Very clever and concise.
// https://discuss.leetcode.com/topic/80623/my-clean-and-concise-c-solution-by-checking-balance-and-maximum 
#include <algorithm>
#include <cmath>
#include <vector>
using std::abs;
using std::max;
using std::vector;

class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        auto &a = machines;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        
        int sum = 0;
        int res = a[0];
        int i;
        for (i = 0; i < n; ++i) {
            sum += a[i];
            res = max(res, a[i]);
        }
        if (sum % n != 0) {
            return -1;
        }
        // Average
        sum /= n;
        
        int balance = 0;
        res -= sum;
        for (i = 0; i < n; ++i) {
            // The trick is here.
            balance += a[i] - sum;
            res = max(res, abs(balance));
        }
        return res;
    }
};
