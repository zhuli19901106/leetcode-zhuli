#include <algorithm>
#include <string>
using std::reverse;
using std::string;

class Solution {
public:
    void reverseWords(string &s) {
        int ls = s.size();
        reverse(s.begin(), s.end());
        int i, j;
        
        i = 0;
        while (i < ls) {
            if (s[i] == ' ') {
                ++i;
                continue;
            }
            j = i + 1;
            while (j < ls && s[j] != ' ') {
                ++j;
            }
            reverse(s.begin() + i, s.begin() + j);
            i = j;
        }
    }
};
