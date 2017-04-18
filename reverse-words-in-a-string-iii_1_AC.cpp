#include <algorithm>
#include <string>
using std::reverse;
using std::string;

class Solution {
public:
    string reverseWords(string s) {
        int ls = s.size();
        int i, j;
        
        i = 0;
        while (i < ls) {
            while (i < ls && s[i] == ' ') {
                ++i;
            }
            j = i + 1;
            while (j < ls && s[j] != ' ') {
                ++j;
            }
            reverse(s.begin() + i, s.begin() + j);
            i = j;
        }
        
        return s;
    }
};
