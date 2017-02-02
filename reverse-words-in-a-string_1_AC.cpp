#include <algorithm>
using std::reverse;

class Solution {
public:
    void reverseWords(string &s) {
        int ls = s.size();
        int i, j;
        
        i = 0;
        j = 0;
        while (i < ls && s[i] == ' ') {
            ++i;
        }
        while (i < ls) {
            while (i < ls && s[i] != ' ') {
                s[j++] = s[i++];
            }
            if (i == ls) {
                break;
            }
            while (i < ls && s[i] == ' ') {
                ++i;
            }
            s[j++] = ' ';
        }
        s.resize(j);
        ls = s.size();
        
        i = 0;
        while (i < ls) {
            while (i < ls && s[i] == ' ') {
                ++i;
            }
            if (i == ls) {
                break;
            }
            j = i + 1;
            while (j < ls && s[j] != ' ') {
                ++j;
            }
            reverse(s.begin() + i, s.begin() + j);
            i = j;
        }
        while (s.size() > 0 && s.back() == ' ') {
            s.pop_back();
        }
        reverse(s.begin(), s.end());
    }
};
