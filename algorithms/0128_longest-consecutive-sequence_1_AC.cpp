// Hash it
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using std::max;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        
        unordered_map<int, int> m1, m2;
        unordered_set<int> us;
        int i;
        
        bool has_left, has_right;
        int left, right;
        for (i = 0; i < n; ++i) {
            if (us.find(nums[i]) != us.end()) {
                continue;
            }
            us.insert(nums[i]);
            has_left = has_right = false;
            
            if (m2.find(nums[i] - 1) != m2.end()) {
                has_left = true;
                left = m2[nums[i] - 1];
            } else {
                left = nums[i];
            }
            if (m1.find(nums[i] + 1) != m1.end()) {
                has_right = true;
                right = m1[nums[i] + 1];
            } else {
                right = nums[i];
            }
            
            m1[left] = right;
            m2[right] = left;
            if (has_left) {
                m2.erase(nums[i] - 1);
            }
            if (has_right) {
                m1.erase(nums[i] + 1);
            }
        }
        
        int res = 0;
        for (auto it = m1.begin(); it != m1.end(); ++it) {
            res = max(res, it->second - it->first + 1);
        }
        m1.clear();
        m2.clear();
        us.clear();
        
        return res;
    }
};
