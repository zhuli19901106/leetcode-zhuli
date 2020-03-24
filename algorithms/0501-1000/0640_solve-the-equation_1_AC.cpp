#include <string>
using std::string;

class Solution {
public:
    string solveEquation(string equation) {
        auto &s = equation;
        int ls = s.size();
        
        int pe = s.find('=');
        string s1 = s.substr(0, pe);
        string s2 = s.substr(pe + 1, ls - pe - 1);
        
        int a1, b1;
        parse(s1, a1, b1);
        int a2, b2;
        parse(s2, a2, b2);
        
        if (a1 != a2) {
            return "x=" + to_string((b2 - b1) / (a1 - a2));
        } else if (b1 == b2) {
            return string("Infinite solutions");
        } else {
            return string("No solution");
        }
    }
private:
    void parse(string s, int &a, int &b) {
        if (s[0] != '+' && s[0] != '-') {
            s = '+' + s;
        }
        
        string ss = "";
        int ls = s.size();
        int i;
        int sign;
        int coef;
        
        i = 0;
        a = 0;
        b = 0;
        while (i < ls) {
            sign = (s[i++] == '-' ? -1 : +1);
            while (i < ls && s[i] != '+' && s[i] != '-') {
                ss.push_back(s[i++]);
            }
            if (sscanf(ss.data(), "%d", &coef) != 1) {
                coef = 1;
            }
            if (ss.back() == 'x') {
                a += sign * coef;
            } else {
                b += sign * coef;
            }
            ss.clear();
        }
    }
};
