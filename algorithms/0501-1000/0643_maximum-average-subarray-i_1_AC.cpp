#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum;
        int n = nums.size();
        int i;
        
        sum = 0;
        i = 0;
        while (i < k) {
            sum += nums[i];
            ++i;
        }
        
        double res = sum;
        while (i < n) {
            sum += (nums[i] - nums[i - k]);
            res = max(res, sum);
            ++i;
        }
        
        return res / k;
    }
};
