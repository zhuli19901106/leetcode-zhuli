// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#include <cmath>
using std::ceil;
using std::log10;

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (const int &x: nums) {
            if ((countDigits(x) & 1) == 0) {
                ++count;
            }
        }
        return count;
    }
private:
    int countDigits(int x) {
        if (x > 0) {
            return int(floor(log10(1.0 * x))) + 1;
        } else if (x < 0) {
            return countDigits(-x);
        } else {
            return 1;
        }
    }
};
