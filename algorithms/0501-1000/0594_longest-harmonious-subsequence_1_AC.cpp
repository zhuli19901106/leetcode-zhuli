#include <algorithm>
#include <vector>
using std::max;
using std::sort;
using std::vector;

class Solution {
public:
    int findLHS(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n < 2) {
            return 0;
        }
        sort(a.begin(), a.end());
        
        int i, j;
        int res = 0;
        int val;
        
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && a[j] - a[i] <= 1) {
                ++j;
            }
            if (j - 1 > i && a[j - 1] - a[i] == 1) {
                res = max(res, j - i);
            }
            val = a[i];
            while (i < j && a[i] == val) {
                ++i;
            }
        }
        
        return res;
    }
};
