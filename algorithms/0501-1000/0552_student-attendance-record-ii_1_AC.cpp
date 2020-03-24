// Is there an O(1) solution?
#include <cstdint>

static const int64_t MOD = 1000000007;

class Solution {
public:
    int checkRecord(int n) {
        if (n < 2) {
            return 3 * n;
        }
        
        vector<int64_t> v(n + 1);
        v[0] = 1;
        v[1] = 2;
        v[2] = 4;
        
        int64_t a[4], a1[4];
        int i, j;
        
        for (i = 0; i < 4; ++i) {
            a[i] = 1;
        }
        for (i = 3; i <= n; ++i) {
            a1[0] = (a[0] + a[2]) % MOD;
            a1[1] = (a[0] + a[2]) % MOD;
            a1[2] = (a[1] + a[3]) % MOD;
            a1[3] = (a[1]) % MOD;
            v[i] = 0;
            for (j = 0; j < 4; ++j) {
                a[j] = a1[j];
                v[i] += a[j];
            }
            v[i] %= MOD;
        }
        
        int64_t res = v[n];
        for (i = 0; i < n; ++i) {
            res = (res + v[i] * v[n - 1 - i]) % MOD;
        }
        v.clear();
        
        return res;
    }
};
