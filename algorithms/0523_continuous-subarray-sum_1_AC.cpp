#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        auto &a = nums;
        int n = a.size();
        int i;
        if (k == 0) {
            int cc;
            i = 0;
            while (i < n) {
                if (a[i] != 0) {
                    ++i;
                    continue;
                }
                cc = 0;
                while (i < n && a[i] == 0) {
                    ++i;
                    ++cc;
                }
                if (cc >= 2) {
                    return true;
                }
            }
            return false;
        }
        
        unordered_map<int, int> um;
        um[0] = 0;
        int sum = 0;
        for (i = 0; i < n; ++i) {
            sum = (sum + a[i]) % k;
            if (um.find(sum) == um.end()) {
                um[sum] = i + 1;
            }
            if (i + 1 - um[sum] >= 2) {
                break;
            }
        }
        um.clear();
        
        return i < n;
    }
};
