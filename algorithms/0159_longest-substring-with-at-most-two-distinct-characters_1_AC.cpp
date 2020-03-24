#include <algorithm>
#include <string>
#include <vector>
using std::max;
using std::string;
using std::vector;

class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        const int k = 2;
        int ls = s.size();
        if (ls <= k) {
            return ls;
        }
        
        static const int DICT_SIZE = 256;
        vector<int> c(DICT_SIZE, 0);
        int i, j;
        int cc = 0;
        int res = 0;
        
        j = 0;
        for (i = 0; i < ls; ++i) {
            if (c[s[i]] == 0) {
                ++cc;
            }
            ++c[s[i]];
            if (cc <= k) {
                res = max(res, i - j + 1);
            }
            while (cc > k) {
                if (c[s[j]] == 1) {
                    --cc;
                }
                --c[s[j++]];
            }
        }
        c.clear();
        
        return res;
    }
};
