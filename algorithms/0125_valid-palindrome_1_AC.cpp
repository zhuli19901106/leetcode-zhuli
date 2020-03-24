#include <cctype>
using std::isalnum;
using std::isupper;
using std::tolower;

class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            if (!isalnum(s[i])) {
                ++i;
            } else if (!isalnum(s[j])) {
                --j;
            } else if (isupper(s[i])) {
                s[i] = tolower(s[i]);
            } else if (isupper(s[j])) {
                s[j] = tolower(s[j]);
            } else if (s[i] != s[j]) {
                return false;
            } else {
                ++i;
                --j;
            }
        }
        return true;
    }
};
