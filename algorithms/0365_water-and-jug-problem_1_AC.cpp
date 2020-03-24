class Solution {
public:
    bool canMeasureWater(int x, int y, int z) {
        if (z == 0) {
            return true;
        }
        if (x == 0) {
            return y == z;
        }
        if (y == 0) {
            return x == z;
        }
        if (x + y < z) {
            return false;
        }
        int d = gcd(x, y);
        return z % d == 0;
    }
private:
    int gcd(int x, int y) {
        int t;
        while (x % y != 0) {
            t = x;
            x = y;
            y = t % y;
        }
        return y;
    }
};
