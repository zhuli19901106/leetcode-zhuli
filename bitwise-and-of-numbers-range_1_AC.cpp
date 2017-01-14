class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if (m == 0) {
            return 0;
        }
        int x = n;
        while (x > m) {
            x = (x & x - 1);
        }
        return x;
    }
};
