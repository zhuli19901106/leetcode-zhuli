#include <algorithm>
using std::max;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> &a = heights;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        vector<int> ll(n), rr(n);
        
        int i, j;
        ll[0] = 0;
        for (i = 1; i <= n - 1; ++i) {
            ll[i] = i;
            j = i;
            while (ll[j] - 1 >= 0 && a[ll[j] - 1] >= a[i]) {
                j = ll[j] - 1;
            }
            ll[i] = ll[j];
        }
        
        rr[n - 1] = n - 1;
        for (i = n - 2; i >= 0; --i) {
            rr[i] = i;
            j = i;
            while (rr[j] + 1 <= n - 1 && a[rr[j] + 1] >= a[i]) {
                j = rr[j] + 1;
            }
            rr[i] = rr[j];
        }
        
        int max_area = 0;
        for (i = 0; i < n; ++i) {
            max_area = max(max_area, a[i] * (rr[i] - ll[i] + 1));
        }
        ll.clear();
        rr.clear();
        return max_area;
    }
};
