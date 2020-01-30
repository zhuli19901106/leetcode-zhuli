// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
#include <string>
using std::to_string;

class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int product = 1;
        int sum = 0;
        for (auto &ch: s) {
            product *= (ch - '0');
            sum += (ch - '0');
        }
        return product - sum;
    }
};
