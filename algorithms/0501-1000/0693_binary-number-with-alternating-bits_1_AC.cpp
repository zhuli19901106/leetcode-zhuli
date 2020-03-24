#include <cstdint>

class Solution {
public:
    bool hasAlternatingBits(int n) {
        int64_t n1 = n;
        if (n1 & 1) {
            return isPowerOfTwo(1 + n1 + (n1 << 1));
        } else {
            return isPowerOfTwo(1 + n1 + (n1 >> 1));
        }
    }
private:
    bool isPowerOfTwo(int64_t n) {
        int c = 0;
        while (n != 0) {
            n = n & n - 1;
            ++c;
        }
        return c == 1;
    }
};
