#include <algorithm>
#include <climits>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        
        // v1 for max, v2 for min
        vector<vector<int>> v1(2, vector<int>(n)), v2(2, vector<int>(n));
        const int k = 3;
        
        int f, nf;
        int i;
        f = 1;
        nf = !f;
        v1[nf][0] = v2[nf][0] = a[0];
        for (i = 1; i < n; ++i) {
            v1[nf][i] = max(v1[nf][i - 1], a[i]);
            v2[nf][i] = min(v2[nf][i - 1], a[i]);
        }
        
        int p1, p2;
        int j;
        for (i = 1; i < k; ++i) {
            v1[f][i - 1] = INT_MIN;
            v2[f][i - 1] = INT_MAX;
            for (j = i; j < n; ++j) {
                p1 = v1[nf][j - 1] * a[j];
                p2 = v2[nf][j - 1] * a[j];
                v1[f][j] = max(v1[f][j - 1], max(p1, p2));
                v2[f][j] = min(v2[f][j - 1], min(p1, p2));
            }
            f = !f;
            nf = !f;
        }
        
        int res = v1[nf][n - 1];
        v1.clear();
        v2.clear();
        
        return res;
    }
};
