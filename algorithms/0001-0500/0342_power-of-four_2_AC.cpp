// Using logarithm
#include <cmath>
using std::log10;

class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num <= 0) {
            return false;
        }
        int lg = int(log10(1.0 * num) / log10(4.0));
        return 1 << (2 * lg) == num;
    }
};
