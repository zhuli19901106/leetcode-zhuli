#include <string>
using std::string;
using std::to_string;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int n = nums.size();
        int i, j;
        
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && nums[j] == nums[j - 1] + 1) {
                ++j;
            }
            if (j - i == 1) {
                res.push_back(to_string(nums[i]));
            } else {
                res.push_back(to_string(nums[i]) + "->" + to_string(nums[j - 1]));
            }
            i = j;
        }
        return res;
    }
};
