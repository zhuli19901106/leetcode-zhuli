#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        auto &vp = prices;
        int n = vp.size();
        
        int max_sum = 0;
        int min_p = vp[0];
        int i;
        for (i = 1; i < n; ++i) {
            max_sum = max(max_sum, vp[i] - min_p - fee);
            min_p = min(min_p, vp[i] - max_sum);
        }
        return max_sum;
    }
};
