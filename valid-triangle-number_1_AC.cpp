#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        
        sort(a.begin(), a.end());
        int i, j, k;
        int sum = 0;
        
        i = 0;
        while (i < n && a[i] <= 0) {
            ++i;
        }
        while (i + 2 < n) {
            k = i + 2;
            for (j = i + 1; j + 1 < n; ++j) {
                while (k < n && a[i] + a[j] > a[k]) {
                    ++k;
                }
                sum += k - (j + 1);
            }
            ++i;
        }
        
        return sum;
    }
};
