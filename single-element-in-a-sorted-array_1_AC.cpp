#include <vector>
using std::vector;

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        
        int ll = 0;
        int rr = n - 1;
        int mm;
        
        while (ll <= rr) {
            mm = ll + (rr - ll >> 2 << 1);
            if (mm + 1 <= n - 1 && a[mm] == a[mm + 1]) {
                ll = mm + 2;
            } else if (mm - 1 >= 0 && a[mm] == a[mm - 1]) {
                rr = mm - 2;
            } else {
                return a[mm];
            }
        }
        // not supposed to be here
        return -1;
    }
};
