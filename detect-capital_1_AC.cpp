#include <cctype>
using std::islower;
using std::isupper;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int uc = 0, lc = 0;
        int lw = word.size();
        int i;
        for (i = 0; i < lw; ++i) {
            if (islower(word[i])) {
                ++lc;
            } else if (isupper(word[i])) {
                ++uc;
                if (lc > 0) {
                    return false;
                }
            }
        }
        return lc == 0 || uc <= 1;
    }
};
