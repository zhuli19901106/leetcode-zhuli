#include <cstdint>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t r = 0u;
        int i;
        for (i = 0; i < 32; ++i) {
            r = (r << 1u) | (n & 1u);
            n >>= 1u;
        }
        return r;
    }
};
