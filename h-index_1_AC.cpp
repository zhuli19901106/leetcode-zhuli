#include <algorithm>
using std::sort;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        vector<int> &a = citations;
        sort(a.begin(), a.end());
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        
        int ll, mm, rr;
        if (a[n - 1] < 1) {
            return 0;
        }
        if (a[0] >= n) {
            return n;
        }
        
        ll = 0;
        rr = n;
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            if (a[n - mm] >= mm) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return ll;
    }
};
