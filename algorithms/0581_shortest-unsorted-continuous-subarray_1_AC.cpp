#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n < 2) {
            return 0;
        }
        
        vector<int> v(n);
        int i;
        v[n - 1] = a[n - 1];
        for (i = n - 2; i >= 0; --i) {
            v[i] = min(v[i + 1], a[i]);
        }
        
        int left = 0;
        while (left <= n - 1 && v[left] == a[left]) {
            ++left;
        }
        
        v[0] = a[0];
        for (i = 1; i <= n - 1; ++i) {
            v[i] = max(v[i - 1], a[i]);
        }
        
        int right = n - 1;
        while (right >= left && v[right] == a[right]) {
            --right;
        }
        
        v.clear();
        return right - left + 1;
    }
};
