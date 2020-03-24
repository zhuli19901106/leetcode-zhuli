// Permutation group.
#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        vector<bool> vb(n, false);
        
        int i, j;
        int res;
        int cnt;
        
        res = 0;
        j = 0;
        while (j < n) {
            if (vb[j]) {
                ++j;
                continue;
            }
            
            i = j;
            cnt = 0;
            while (!vb[i]) {
                vb[i] = true;
                i = nums[i];
                ++cnt;
            }
            res = max(res, cnt);
            ++j;
        }
        vb.clear();
        
        return res;
    }
};
