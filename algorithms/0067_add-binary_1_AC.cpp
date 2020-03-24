#include <algorithm>
using std::swap;

class Solution {
public:
    string addBinary(string a, string b) {
        if (a.size() > b.size()) {
            swap(a, b);
        }
        int la = a.size();
        int lb = b.size();
        string c = "";
        
        c.resize(lb + 1, 0);
        int i;
        for (i = 0; i < la; ++i) {
            c[i] = a[la - 1 - i] - '0';
        }
        for (i = 0; i < lb; ++i) {
            c[i] += b[lb - 1 - i] - '0';
        }
        for (i = 0; i < lb; ++i) {
            c[i + 1] += c[i] / 2;
            c[i] %= 2;
        }
        while (c.size() > 1 && c.back() == 0) {
            c.pop_back();
        }
        int lc = c.size();
        for (i = 0; i < lc; ++i) {
            c[i] += '0';
        }
        reverse(c.begin(), c.end());
        return c;
    }
};
