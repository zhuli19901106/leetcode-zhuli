#include <cstdint>
#include <vector>
using std::vector;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        auto &a = nums;
        int n = a.size();
        
        int64_t s = 1;
        int res = 0;
        int i, j;
        i = j = 0;
        while (i < n) {
            while (j < n && s * a[j] < k) {
                s *= a[j++];
            }
            res += j - i;
            if (i < j) {
                s /= a[i];
            }
            ++i;
            if (j < i) {
                j = i;
            }
        }
        
        return res;
    }
};
