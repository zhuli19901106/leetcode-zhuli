#include <algorithm>
using std::min;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        auto &a = timeSeries;
        int n = a.size();
        int res = 0;
        if (n == 0) {
            return res;
        }
        int i;
        for (i = 0; i < n - 1; ++i) {
            res += min(duration, a[i + 1] - a[i]);
        }
        res += duration;
        return res;
    }
};
