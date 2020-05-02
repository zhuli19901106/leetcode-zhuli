#include <algorithm>
#include <vector>
using std::max;
using std::reverse;
using std::sort;
using std::vector;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        auto &a = nums;
        int n = a.size();
        if (n == 0) {
            return false;
        }
        if (k == 1) {
            return true;
        }
        
        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
        
        int i;
        int sum = 0;
        int max_val = a[0];
        for (i = 0; i < n; ++i) {
            sum += a[i];
            max_val = max(max_val, a[i]);
        }
        if (sum % k != 0 || max_val > sum / k) {
            return false;
        }
        sum /= k;
        
        vector<int> v(k, sum);
        return dfs(a, 0, v, k);
    }
private:
    bool dfs(vector<int> &a, int idx, vector<int> &v, int k) {
        if (idx == a.size()) {
            return true;
        }
        int ki;
        for (ki = 0; ki < k; ++ki) {
            if (v[ki] < a[idx]) {
                continue;
            }
            v[ki] -= a[idx];
            if (dfs(a, idx + 1, v, k)) {
                return true;
            }
            v[ki] += a[idx];
        }
        return false;
    }
};
