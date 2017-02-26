// This clever solution is from @NathanNi
// https://discuss.leetcode.com/topic/64624/concise-easy-to-understand-java-5ms-solution-with-explaination
#include <algorithm>
#include <cstdint>
using std::min;

class Solution {
public:
    int findKthNumber(int n, int k) {
        --k;
        
        int res = 1;
        int d;
        while (k > 0) {
            d = calc(n, res);
            if (k >= d) {
                k -= d;
                // Go right
                res += 1;
            } else {
                k -= 1;
                // Go down
               res *= 10;
            }
        }
        return res;
    }
private:
    int calc(int64_t n, int64_t n1) {
        int64_t n2 = n1 + 1;
        int res = 0;
        while (n1 <= n) {
            // The key is here
            res += min(n + 1, n2) - n1;
            n1 *= 10;
            n2 *= 10;
        }
        return res;
    }
};
