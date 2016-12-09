// Fibonacci
class Solution {
public:
    int climbStairs(int n) {
        if (n < 0) {
            return 0;
        }
        int f1 = 0;
        int f2 = 1;
        int f3 = 1;
        int i;
        for (i = 0; i < n; ++i) {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
};
