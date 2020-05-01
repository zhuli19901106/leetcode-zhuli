// O(n) time complexity
#include <algorithm>
using std::next;
using std::nth_element;
using std::swap;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return;
        }
        auto it = next(nums.begin(), n >> 1);
        nth_element(nums.begin(), it, nums.end());
        int i, j, k;
        
        int pivot = nums[n / 2];
        vector<int> v(n);
        j = (n & 1) == 1 ? n - 1 : n - 2;
        for (i = 0; i < n; ++i) {
            if (nums[i] < pivot) {
                v[j] = nums[i];
                j -= 2;
            }
        }
        k = 1;
        for (i = 0; i < n; ++i) {
            if (nums[i] > pivot) {
                v[k] = nums[i];
                k += 2;
            }
        }
        while (j >= 0) {
            v[j] = pivot;
            j -= 2;
        }
        while (k <= n - 1) {
            v[k] = pivot;
            k += 2;
        }
        nums = v;
    }
};
