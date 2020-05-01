#include <cstdint>

class Solution {
public:
    int uniquePaths(int m, int n) {
        return combination(n + m - 2, n - 1);
    }
private:
    int64_t combination(int n, int k) {
        if (k > n / 2) {
            return combination(n, n - k);
        }
        int64_t sum = 1;
        int i;
        for (i = 1; i <= k; ++i) {
            sum *= (n + 1 - i);
            sum /= i;
        }
        return sum;
    }
};
