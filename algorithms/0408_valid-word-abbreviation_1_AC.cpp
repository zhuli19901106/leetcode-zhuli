#include <cctype>
#include <string>
using std::isdigit;
using std::islower;
using std::string;

class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int lw = word.size();
        int la = abbr.size();
        int i = 0;
        int j = 0;
        int d;
        while (i < lw && j < la) {
            if (isdigit(abbr[j])) {
                // Leading zero
                if (abbr[j] == '0' && j + 1 < la && isdigit(abbr[j + 1])) {
                    return false;
                }
                d = 0;
                while (j < la && isdigit(abbr[j])) {
                    d = d * 10 + (abbr[j++] - '0');
                }
                if (d == 0) {
                    return false;
                }
                
                i += d;
            } else {
                if (word[i] != abbr[j]) {
                    return false;
                } else {
                    ++i;
                    ++j;
                }
            }
        }
        return i == lw && j == la;
    }
};
