#include <vector>
using std::vector;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n == 1) {
            return 0;
        }
        
        int ll = 0;
        int rr = n - 1;
        int mm;
        bool bl, br;
        while (ll <= rr) {
            mm = ll + (rr - ll >> 1);
            bl = (mm == 0 || a[mm - 1] < a[mm]);
            br = (mm == n - 1 || a[mm + 1] < a[mm]);
            if (bl && br) {
                return mm;
            } else if (bl && !br) {
                ll = mm + 1;
            } else if (!bl && br) {
                rr = mm - 1;
            } else {
                // Both are fine.
                rr = mm - 1;
            }
        }
        return -1;
    }
};
