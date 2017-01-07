class Solution {
public:
    int lastRemaining(int n) {
        int ll = 1;
        int rr = n;
        int d = 1;
        int cnt = n;
        bool rev = false;
        while (cnt > 1) {
            if (rev) {
                if (cnt & 1) {
                    ll += d;
                }
                rr -= d;
            } else {
                ll += d;
                if (cnt & 1) {
                    rr -= d;
                }
            }
            cnt >>= 1;
            d <<= 1;
            rev = !rev;
        }
        return ll;
    }
};
