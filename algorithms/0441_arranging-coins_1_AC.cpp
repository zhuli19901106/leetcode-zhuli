#include <cmath>
using std::sqrt;

class Solution {
public:
    int arrangeCoins(int n) {
        if (n <= 0) {
            return 0;
        }
        return int((sqrt(8.0 * n + 1.0) - 1.0) / 2.0);
    }
};
