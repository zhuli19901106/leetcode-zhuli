// Do you know why we need Numerical Analysis?
// Because precision problem is a major headache.
// And don't forget integer overflow.
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <string>
using std::log;
using std::pow;
using std::sscanf;
using std::string;
using std::to_string;

class Solution {
public:
    string smallestGoodBase(string n) {
        // m = (k ^ (t + 1) - 1) / (k - 1)
        // (k, t) = (?, ?)
        int64_t m;
        sscanf(n.data(), "%lld", &m);
        
        int64_t t1 = 1;
        int64_t t2 = (int)(log2(m + 1) - 1);
        int64_t k, t;
        for (t = t2; t >= t1; --t) {
            k = solveK(m, t);
            if (m == sum(k, t)) {
                return to_string(k);
            }
        }
        return to_string(m - 1);
    }
private:
    double log2(double x) {
        return log(x) / log(2.0);
    }
    
    int64_t solveK(int64_t m, int64_t t) {
        int64_t low = 2;
        int64_t high = pow(1.0 * m, 1.0 / t) + 1;
        int64_t k;
        
        while (high - low > 1) {
            k = low + (high - low >> 1);
            if (sum(k, t) <= m) {
                low = k;
            } else {
                high = k;
            }
        }
        return low;
    }
    
    int64_t powll(int64_t x, int64_t y) {
        if (x == 0) {
            return 0;
        }
        if (y == 0) {
            return 1;
        }
        
        int64_t p = powll(x, y >> 1);
        int64_t res = p * p;
        if (y & 1) {
            res *= x;
        }
        return res;
    }
    
    int64_t sum(int64_t k, int64_t t) {
        int64_t s = 0;
        int64_t bs = 1;
        int64_t i;
        
        for (i = 0; i <= t; ++i) {
            s += bs;
            bs *= k;
        }
        return s;
    }
};
