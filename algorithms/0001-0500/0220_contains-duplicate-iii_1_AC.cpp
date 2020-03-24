// So many edge cases, what a headache...
// Still, balanced BST is good stuff.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <map>
using std::abs;
using std::map;
using std::min;
using std::next;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k < 0 || t < 0) {
            return false;
        }
        ++k;
        int n = nums.size();
        if (n < 2) {
            return false;
        }
        
        map<int, int> mm;
        bool found = false;
        
        k = min(k, n);
        
        int i = 0;
        while (!found && i < k) {
            ++mm[nums[i]];
            if(checkNearby(mm, nums[i], t)) {
                found = true;
            }
            ++i;
        }
        while (!found && i < n) {
            --mm[nums[i - k]];
            if (mm[nums[i - k]] == 0) {
                mm.erase(nums[i - k]);
            }
            ++mm[nums[i]];
            if(checkNearby(mm, nums[i], t)) {
                found = true;
            }
            ++i;
        }
        mm.clear();
        
        return found;
    }
private:
    bool checkNearby(map<int, int> &mm, int num1, int diff) {
        auto it = mm.find(num1);
        if (it->second > 1) {
            return true;
        }
        
        int num2;
        if (it != mm.begin()) {
            --it;
            num2 = it->first;
            ++it;
            if (abs((int64_t)num1 - num2) <= diff) {
                return true;
            }
        }
        if (next(it) != mm.end()) {
            ++it;
            num2 = it->first;
            --it;
            if (abs((int64_t)num1 - num2) <= diff) {
                return true;
            }
        }
        
        return false;
    }
};
