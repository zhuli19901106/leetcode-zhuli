class Solution {
public:
    int numDecodings(string s) {
        static const int LOW = 1;
        static const int HIGH = 26;
        
        int ls = s.size();
        if (ls == 0) {
            return 0;
        }
        int f1 = 0;
        int f2 = 1;
        int f3;
        
        int i;
        int d;
        for (i = 0; i < ls; ++i) {
            f3 = 0;
            d = (s[i] - '0');
            if (d >= LOW && d <= HIGH) {
                f3 += f2;
            }
            if (i > 0 && s[i - 1] != '0') {
                d = (s[i - 1] - '0') * 10 + (s[i] - '0');
                if (d >= LOW && d <= HIGH) {
                    f3 += f1;
                }
            }
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
};
