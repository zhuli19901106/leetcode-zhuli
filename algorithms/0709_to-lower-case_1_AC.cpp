// to-lower-case
#include <cctype>
using std::isupper;

class Solution {
public:
    string toLowerCase(string str) {
        int ls = str.size();
        for (int i = 0; i < ls; ++i) {
            if (isupper(str[i])) {
                str[i] = str[i] - 'A' + 'a';
            }
        }
        return str;
    }
};
