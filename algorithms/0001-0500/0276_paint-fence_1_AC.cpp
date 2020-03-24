// Make sure you have a finite state machine in your head.
class Solution {
public:
    int numWays(int n, int k) {
        if (n < 2 || k == 0) {
            return n * k;
        }
        
        int same, diff;
        int old_same, old_diff;
        
        old_same = k;
        old_diff = k * k - k;
        int i;
        for (i = 2; i < n; ++i) {
            same = old_diff;
            diff = (k - 1) * (old_same + old_diff);
            old_same = same;
            old_diff = diff;
        }
        return old_same + old_diff;
    }
};
