#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        
        int sum = 0;
        int i;
        for (i = 0; i < n; i += 2) {
            sum += nums[i];
        }
        
        return sum;
    }
};
