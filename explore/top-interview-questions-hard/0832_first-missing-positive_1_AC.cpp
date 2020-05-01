// Use the input array as marker array.
#include <cmath>
using std::abs;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (a[i] < 1 || a[i] > n) {
                a[i] = n + 1;
            }
        }
        
        int val;
        for (i = 0; i < n; ++i) {
            val = abs(a[i]);
            if (val == n + 1) {
                continue;
            }
            if (a[val - 1] > 0) {
                a[val - 1] = -a[val - 1];
            }
        }
        for (i = 0; i < n; ++i) {
            if (a[i] > 0) {
                break;
            }
        }
        
        return i + 1;
    }
};
