#include <algorithm>
using std::next_permutation;
using std::sort;

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
            next_permutation(nums.begin(), nums.end());
        }
        return res;
    }
};
