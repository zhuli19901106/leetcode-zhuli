#include <climits>
#include <cstdint>

class Solution {
public:
    int divide(int dividend, int divisor) {
        int64_t n1 = dividend;
        int64_t n2 = divisor;
        
        if (n1 == 0) {
            return 0;
        }
        
        int flag = 1;
        if (n1 < 0) {
            flag = -flag;
            n1 = -n1;
        }
        if (n2 < 0) {
            flag = -flag;
            n2 = -n2;
        }
        
        int64_t b = 1;
        int64_t d = n2;
        while ((d << 1) <= n1) {
            b <<= 1;
            d <<= 1;
        }
        
        int64_t res = 0;
        while (b > 0) {
            if (n1 >= d) {
                res += b;
                n1 -= d;
            }
            b >>= 1;
            d >>= 1;
        }
        if (flag == -1) {
            res = -res;
        }
        
        if (res < INT_MIN || res > INT_MAX) {
            res = INT_MAX;
        }
        return res;
    }
};
