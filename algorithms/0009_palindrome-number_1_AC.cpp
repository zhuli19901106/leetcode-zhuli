class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        const int R = 10;
        int x1 = x;
        int r = 0;
        while (x1 > 0) {
            r = r * R + x1 % R;
            x1 /= R;
        }
        return r == x;
    }
};
