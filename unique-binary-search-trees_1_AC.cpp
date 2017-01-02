#include <cstdint>

class Solution {
public:
    int numTrees(int n) {
        if (n == 0) {
            return 0;
        }
        return combination(2 * n, n) / (n + 1);
    }
private:
    int64_t combination(int n, int k) {
        if (k > n / 2) {
            return combination(n, n - k);
        }
        
        int64_t sum = 1;
        int i;
        for (i = 1; i <= k; ++i) {
            sum = sum * (n + 1 - i) / i;
        }
        return sum;
    }
};
