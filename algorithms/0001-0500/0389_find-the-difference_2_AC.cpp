#include <algorithm>
using std::sort;

class Solution {
public:
    char findTheDifference(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        int i;
        int n = s.size();
        for (i = 0; i < n; ++i) {
            if (s[i] != t[i]) {
                break;
            }
        }
        return t[i];
    }
};
