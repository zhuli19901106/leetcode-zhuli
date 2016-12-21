#include <algorithm>
#include <climits>
using std::max;
using std::min;
using std::sort;

class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int n = houses.size();
        int m = heaters.size();
        if (n == 0) {
            return 0;
        }
        int res = INT_MIN;
        if (m == 0) {
            return res;
        }
        
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int i;
        int j;
        int r;
        
        j = 0;
        for (i = 0; i < n; ++i) {
            r = INT_MAX;
            while (j < m && heaters[j] < houses[i]) {
                ++j;
            }
            if (j > 0) {
                r = min(r, houses[i] - heaters[j - 1]);
            }
            if (j < m) {
                r = min(r, heaters[j] - houses[i]);
            }
            res = max(res, r);
        }
        return res;
    }
};
