#include <cstdint>

class Solution {
public:
    string convertToTitle(int n) {
        const int R = 26;
        int64_t base = R;
        int64_t cnt = 1;
        
        --n;
        while (n >= base) {
            n -= base;
            base *= R;
            ++cnt;
        }
        string s;
        int i;
        for (i = 0; i < cnt; ++i) {
            base /= R;
            s.push_back('A' + n / base);
            n %= base;
        }
        return s;
    }
};
