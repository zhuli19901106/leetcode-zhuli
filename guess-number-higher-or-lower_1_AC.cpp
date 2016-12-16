// Binary search
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int ll, mm, rr;
        int res;
        
        ll = 1;
        rr = n;
        while(ll <= rr) {
            mm = ll + (rr - ll) / 2;
            // mm = (ll + rr) / 2; // Overflow
            res = guess(mm);
            if (res == -1) {
                rr = mm - 1;
            } else if (res == 1) {
                ll = mm + 1;
            } else {
                return mm;
            }
        }
        // Not found.
        return -1;
    }
};
