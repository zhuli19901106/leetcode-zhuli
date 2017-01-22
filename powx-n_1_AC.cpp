// Ugly
class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0.0 || x == 1.0) {
            return x;
        }
        if (n == 0) {
            return 1.0;
        }
        double y;
        if (n == -n) {
            y = myPow(x, n / 2);
            return y * y;
        }
        if (n < 0) {
            return 1.0 / myPow(x, -n);
        }
        y = myPow(x, n / 2);
        double res = y * y;
        if (n % 2 == 1) {
            res *= x;
        }
        return res;
    }
};
