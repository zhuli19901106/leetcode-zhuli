// Man, that's ugly.
#include <cctype>
#include <string>
using std::isdigit;
using std::string;

class Solution {
public:
    bool isNumber(string s) {
		int ls = s.size();
        int i, j;
        
        i = 0;
        j = ls - 1;
        while (j >= 0 && s[j] == ' ') {
            --j;
        }
        while (i < j && s[i] == ' ') {
            ++i;
        }
        if (i > j) {
            return false;
        }
        s = s.substr(i, j + 1 - i);
        ls = s.size();
        
        int pd, pe;
        int cd, ce;
        
        int k;
        pe = pe = -2;
        cd = ce = 0;
        for (k = 0; k < ls; ++k) {
            if (s[k] == '.') {
                pd = k;
                ++cd;
            } else if (s[k] == 'E' || s[k] == 'e') {
                pe = k;
                ++ce;
            } else if (isdigit(s[k])) {
                continue;
            } else if (issign(s[k]) && (k == 0 || pe == k - 1)) {
                continue;
            } else {
                return false;
            }
        }
        if (cd > 1 || ce > 1) {
            return false;
        }
        if (cd == 1 && ce == 1 && pd > pe) {
            return false;
        }
        
        int cc;
        if (cd == 1) {
            k = pd - 1;
            cc = 0;
            while (k >= 0 && isdigit(s[k])) {
                --k;
                ++cc;
            }
            k = pd + 1;
            while (k < ls && isdigit(s[k])) {
                ++k;
                ++cc;
            }
            if (cc == 0) {
                return false;
            }
        }
        
        if (ce == 1) {
            if (pe == 0 || (pe == 1 && issign(s[0]))) {
                return false;
            }
            k = ls - 1;
            cc = 0;
            while (k > pe && isdigit(s[k])) {
                --k;
                ++cc;
            }
            if (cc == 0) {
                return false;
            }
        }
        
        if (cd == 0 && ce == 0) {
            k = ls - 1;
            cc = 0;
            while (k >= 0 && isdigit(s[k])) {
                --k;
                ++cc;
            }
            if (cc == 0) {
                return false;
            }
        }
        
        return true;
    }
private:
    bool issign(char ch) {
        return ch == '+' || ch == '-';
    }
};
