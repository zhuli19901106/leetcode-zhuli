// Binary search
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int ll = 1;
        int rr = n;
        if (isBadVersion(ll)) {
            return ll;
        }
        if (!isBadVersion(rr)) {
            return n + 1;
        }
        int mm;
        while (rr - ll > 1) {
            mm = ll + (rr - ll) / 2;
            if (isBadVersion(mm)) {
                rr = mm;
            } else {
                ll = mm;
            }
        }
        return rr;
    }
};
