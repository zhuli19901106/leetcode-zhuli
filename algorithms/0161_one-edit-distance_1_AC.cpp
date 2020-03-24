#include <algorithm>
#include <string>
using std::string;
using std::swap;

class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int ls = s.size();
        int lt = t.size();
        if (ls > lt) {
            swap(s, t);
            swap(ls, lt);
        }
        
        if (lt - ls > 1) {
            return false;
        }
        
        int cc = 0;
        int i, j;
        j = 0;
        for (i = 0; i < lt; ++i) {
            if (s[j] == t[i]) {
                ++j;
            } else if (cc == 1) {
                return false;
            } else {
                if (ls == lt) {
                    ++j;
                }
                ++cc;
            }
        }
        return cc == 1;
    }
};
