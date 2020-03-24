#include <algorithm>
#include <cmath>
using std::abs;
using std::sort;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        vector<int> &a = nums;
        int n = a.size();
        if (n < 3) {
            return 0;
        }
        sort(a.begin(), a.end());
        int res = a[0] + a[1] + a[2];
        int i, j, k;
        int val;
        for (i = 0; i < n - 2; ++i) {
            j = i + 1;
            k = n - 1;
            while (j < k) {
                val = a[i] + a[j] + a[k];
                if (abs(val - target) < abs(res - target)) {
                    res = val;
                }
                if (val < target) {
                    ++j;
                } else if (val > target) {
                    --k;
                } else {
                    return target;
                }
            }
        }
        return res;
    }
};
