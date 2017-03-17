#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        auto &a = nums;
        int n = a.size();
        sort(a.begin(), a.end());
        
        int i, j, k;
        int res = 0;
        int sum;
        for (i = 0; i < n - 2; ++i) {
            k = n - 1;
            for (j = i + 1; j < k && j < n - 1; ++j) {
                while (j < k) {
                    sum = a[i] + a[j] + a[k];
                    if (sum < target) {
                        break;
                    }
                    --k;
                }
                res += k - j;
            }
        }
        
        return res;
    }
};
