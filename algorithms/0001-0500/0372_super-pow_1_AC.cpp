#include <cstdint>

class Solution {
public:
    int superPow(int a, vector<int>& b) {
        int64_t res = 1;
        int lb = b.size();
        int i;
        for (i = 0; i < lb; ++i) {
            res = pow(res, R);
            res = res * pow(a, b[i]) % MOD;
        }
        return res;
    }
private:
    static const int64_t R = 10;
    static const int64_t MOD = 1337;
    
    int64_t pow(int64_t x, int64_t y) {
        if (x == 0) {
            return 0;
        }
        if (y == 0) {
            return 1 % MOD;
        }
        int64_t res = pow(x, y >> 1);
        res = res * res % MOD;
        if (y & 1) {
            res = res * x % MOD;
        }
        return res;
    }
};
