// O(n) time and O(1) space
#include <algorithm>
#include <climits>
using std::min;

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        int i;
        for (i = 0; i < n; ++i) {
            sum += nums[i];
        }
        if (sum < s) {
            return 0;
        }
        
        int j;
        int res = INT_MAX;
        
        i = j = 0;
        sum = 0;
        while (j < n) {
            while (j < n && sum < s) {
                sum += nums[j++];
            }
            while (i < j && sum >= s) {
                res = min(res, j - i);
                sum -= nums[i++];
            }
        }
        return res;
    }
};
