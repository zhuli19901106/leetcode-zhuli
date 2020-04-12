#include <algorithm>
#include <climits>
using std::max;
using std::min;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int low = INT_MAX;
        int res = 0;
        int i;
        for (i = 0; i < n; ++i) {
            low = min(low, prices[i]);
            res = max(res, prices[i] - low);
        }
        return res;
    }
};
