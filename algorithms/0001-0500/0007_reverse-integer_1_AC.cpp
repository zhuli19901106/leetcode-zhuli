#include <climits>
#include <cstdint>

class Solution {
public:
    int reverse(int x) {
        const int R = 10;
        
        if (x == INT_MIN) {
            // I forgot this case.
            // x == -x, x == ?
            return 0;
        }
        
        if (x < 0) {
            return -reverse(-x);
        }
        int64_t res = 0;
        while (x > 0) {
            res = res * R + x % R;
            if (res > INT_MAX) {
                return 0;
            }
            x /= R;
        }
        return res;
    }
};
