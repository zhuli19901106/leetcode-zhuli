// Rabin-Karp, simple rolling hashing.
// Strength is apparent, weakness is even more.
// Strong against real-world text matchng, weak against "aaaaaaaaaaaa". 
#include <cstdint>

class Solution {
public:
    int strStr(string haystack, string needle) {
        const string &str = haystack;
        const string &pat = needle;
        int ls = str.size();
        int lp = pat.size();
        if (ls < lp) {
            return -1;
        }
        
        const int64_t R = 37LL;
        const int64_t P = 1000000007LL;
        int64_t hs = 0;
        int64_t hp = 0;
        int64_t base = 1;
        
        int i;
        for (i = 0; i < lp; ++i) {
            base = base * R % P;
        }
        base = (P - base) % P;
        
        for (i = 0; i < lp; ++i) {
            hp = (hp * R + pat[i]) % P;
            hs = (hs * R + str[i]) % P;
        }
        
        int j;
        while (true) {
            if (hs == hp) {
                // Check for false positives
                for (j = 0; j < lp; ++j) {
                    if (str[i - lp + j] != pat[j]) {
                        break;
                    }
                }
                if (j == lp) {
                    return i - lp;
                }
            }
            if (i < ls) {
                hs = (hs * R + str[i - lp] * base + str[i]) % P;
                ++i;
            } else {
                break;
            }
        }
        return -1;
    }
};
