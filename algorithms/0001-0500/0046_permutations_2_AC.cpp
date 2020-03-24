#include <algorithm>
using std::reverse;
using std::sort;
using std::swap;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        int fac = 1;
        int i;
        for (i = 1; i <= n; ++i) {
            fac *= i;
        }
        vector<vector<int>> res;
        
        sort(nums.begin(), nums.end());
        for (i = 0; i < fac; ++i) {
            res.push_back(nums);
            next_permutation(nums, 0, n - 1);
        }
        return res;
    }
private:
    void next_permutation(vector<int> &v, int left, int right) {
        if (left >= right) {
            return;
        }
        int i = right - 1;
        while (i >= left && v[i] >= v[i + 1]) {
            --i;
        }
        if (i < left) {
            reverse(v.begin() + left, v.begin() + right + 1);
            return;
        }
        int j = right;
        while (j >= left && v[j] <= v[i]) {
            --j;
        }
        swap(v[i], v[j]);
        reverse(v.begin() + i + 1, v.begin() + right + 1);
    }
};
