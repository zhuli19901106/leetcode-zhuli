#include <cstring>
using std::memset;

class Solution {
public:
    int longestPalindrome(string s) {
        // Lowercase letters only.
        const int DICT_SIZE = 256;
        int cnt[DICT_SIZE];
        bool has_odd = false;
        
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        int n = s.size();
        int i;
        for (i = 0; i < n; ++i) {
            ++cnt[s[i]];
        }
        
        int res = 0;
        for (i = 0; i < DICT_SIZE; ++i) {
            if (cnt[i] & 1 != 0) {
                has_odd = true;
            }
            res += (cnt[i] >> 1 << 1);
        }
        if (has_odd) {
            ++res;
        }
        return res;
    }
};