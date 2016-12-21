// 4 bits at a time
#include <cstdint>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        static const uint32_t rb[16] = {0u, 8u, 4u, 12u, 2u, 10u, 6u, 14u, 1u, 9u, 5u, 13u, 3u, 11u, 7u, 15u};
        uint32_t r = 0u;
        int i;
        for (i = 0; i < 8; ++i) {
            r = (r << 4u) | (rb[n & 15u]);
            n >>= 4u;
        }
        return r;
    }
};
