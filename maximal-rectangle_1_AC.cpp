#include <algorithm>
using std::max;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        vector<int> a(m, 0);
        
        int i, j;
        int max_area = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (matrix[i][j] == '0') {
                    a[j] = 0;
                } else {
                    a[j] += matrix[i][j] - '0';
                }
            }
            max_area = max(max_area, largestRectangleArea(a));
        }
        return max_area;
    }
private:
    int largestRectangleArea(vector<int> &a) {
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
