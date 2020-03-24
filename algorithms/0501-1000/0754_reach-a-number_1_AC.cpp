// https://leetcode.com/problems/reach-a-number/
// I knew it, brain teaser.
#include <cmath>
using std::ceil;
using std::sqrt;

class Solution {
public:
    int reachNumber(int target) {
        if (target < 0) {
            target = -target;
        }
        int i = (int) ceil((sqrt(8.0 * target + 1) - 1) / 2.0);
        int64_t sum = 1LL * i * (i + 1) / 2;
        ++i;
        while (sum < target || (sum - target) % 2 != 0) {
            sum += i;
            ++i;
        }
        return i - 1;
    }
};
