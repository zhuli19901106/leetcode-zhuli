#include <algorithm>
#include <cstdio>
#include <string>
using std::sscanf;
using std::string;
using std::swap;
using std::to_string;

class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int ls = s.size();
        int i, mi;
        int si;
        for (si = 0; si < ls - 1; ++si) {
            mi = si;
            for (i = si + 1; i < ls; ++i) {
                // watch out
                if (s[i] > s[si] && s[i] >= s[mi]) {
                    mi = i;
                }
            }
            if (mi != si) {
                swap(s[si], s[mi]);
                break;
            }
        }
        
        int num1;
        sscanf(s.data(), "%d", &num1);
        return num1;
    }
};
