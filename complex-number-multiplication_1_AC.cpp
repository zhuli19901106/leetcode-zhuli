#include <cstdio>
#include <string>
using std::sprintf;
using std::sscanf;
using std::string;

class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int xa, ya;
        int xb, yb;
        sscanf(a.data(), "%d+%di", &xa, &ya);
        sscanf(b.data(), "%d+%di", &xb, &yb);
        
        int xc, yc;
        xc = xa * xb - ya * yb;
        yc = xa * yb + ya * xb;
        char buf[30];
        sprintf(buf, "%d+%di", xc, yc);
        
        return string(buf);
    }
};
