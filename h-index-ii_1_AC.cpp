class Solution {
public:
    int hIndex(vector<int>& citations) {
        // Already sorted?
        // I was gonna sort it anyway.
        vector<int> &a = citations;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        if (a[0] >= n) {
            return n;
        }
        if (a[n - 1] < 1) {
            return 0;
        }
        int ll = 0;
        int rr = n;
        int mm;
        
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
