// It never hurts to hash.
#include <cstdint>
#include <string>
using std::string;

class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        const int64_t P = 31;
        
        int la = A.size();
        int lb = B.size();
        int cnt = 0;
        
        int i;
        int64_t hb = 0;
        for (i = 0; i < lb; ++i) {
            hb = hb * P + (B[i] - 'a' + 1);
        }
        
        int64_t base = 1;
        for (i = 0; i < lb; ++i) {
            base *= P;
        }
        
        int64_t ha = 0;
        i = 0;
        while (i < la + lb) {
            if (i % la == 0) {
                ++cnt;
            }
            
            ha = ha * P + (A[i % la] - 'a' + 1);
            if (i >= lb) {
                ha = ha - (A[(i - lb) % la] - 'a' + 1) * base;
            }
            
            if (ha == hb) {
                // a match is found
                return cnt;
            } else {
                ++i;
            }
        }
        return -1;
    }
};
