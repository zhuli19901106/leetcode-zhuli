class Solution {
public:
    bool isPerfectSquare(int num) {
        int ll = 1;
        int rr = num;
        int mm;
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            if (mm <= num / mm) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return ll * ll == num;
    }
};
