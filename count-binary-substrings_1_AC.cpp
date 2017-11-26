#include <algorithm>
using std::min;

class Solution {
public:
    int countBinarySubstrings(string s) {
        char ch;
        int c, last_c = 0;
        int res = 0;
        int ls = s.size();
        int i = 0;
        while (i < ls) {
            ch = s[i];
            c = 0;
            while (i < ls && s[i] == ch) {
                ++c;
                ++i;
            }
            res += min(c, last_c);
            last_c = c;
        }
        return res;
    }
};
