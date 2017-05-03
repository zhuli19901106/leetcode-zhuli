#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int r0 = nums.size();
        int c0 = (r0 != 0 ? nums[0].size() : 0);
        
        if (r0 * c0 != r * c) {
            return nums;
        }
        
        vector<vector<int>> nums1(r, vector<int>(c));
        int i, j;
        int idx;
        for (i = 0; i < r; ++i) {
            for (j = 0; j < c; ++j) {
                idx = i * c + j;
                nums1[i][j] = nums[idx / c0][idx % c0];
            }
        }
        
        return nums1;
    }
};
