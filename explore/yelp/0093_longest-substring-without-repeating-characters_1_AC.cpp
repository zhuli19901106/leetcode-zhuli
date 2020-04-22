#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        static const int DICT_SIZE = 256;
        
        int ls = s.size();
        if (ls < 2) {
            return ls;
        }
        
        vector<int> c(DICT_SIZE, 0);
        int i, j;
        int res = 0;
        j = 0;
        for (i = 0; i < ls; ++i) {
            ++c[s[i]];
            if (c[s[i]] > 1) {
                while (c[s[i]] > 1) {
                    --c[s[j++]];
                }
            }
            res = max(res, i - j + 1);
        }
        c.clear();
        return res;
    }
};
