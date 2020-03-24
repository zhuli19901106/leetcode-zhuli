// Brute-force, I don't wanna bother those fancy tricks.
#include <string>
using std::string;

class Solution {
public:
    int countSubstrings(string s) {
        int ls = s.size();
        int i, j;
        int sum = 0;
        for (i = 0; i < ls; ++i) {
            j = 1;
            while (i - j >= 0 && i + j <= ls - 1 && s[i - j] == s[i + j]) {
                ++j;
            }
            sum += j;
        }
        for (i = 0; i + 1 < ls; ++i) {
            j = 0;
            while (i - j >= 0 && i + 1 + j <= ls - 1 && s[i - j] == s[i + 1 + j]) {
                ++j;
            }
            sum += j;
        }
        return sum;
    }
};
