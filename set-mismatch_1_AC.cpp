// In-place hashing.
#include <cstdint>
#include <vector>
using std::vector;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        int i;
        int m = n + 1;
        for (i = 0; i < n; ++i) {
            a[a[i] % m - 1] += m;
        }
        
        int dup, mis;
        for (i = 0; i < n; ++i) {
            if (a[i] / m > 1) {
                dup = i + 1;
            }else if (a[i] / m < 1) {
                mis = i + 1;
            }
        }
        for (i = 0; i < n; ++i) {
            a[i] %= m;
        }
        
        vector<int> res;
        res.push_back(dup);
        res.push_back(mis);
        
        return res;
    }
};
