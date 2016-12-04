#include <cstring>
using std::memset;

class Solution {
public:
    char findTheDifference(string s, string t) {
        // Only lowercase letters.
        const int DICT_SIZE = 26;
        int cnt[DICT_SIZE];
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        
        int ns = s.size();
        int i;
        for (i = 0; i < ns; ++i) {
            --cnt[s[i] - 'a'];
        }
        int nt = t.size();
        for (i = 0; i < nt; ++i) {
            ++cnt[t[i] - 'a'];
        }
        for (i = 0; i < DICT_SIZE; ++i) {
            if (cnt[i] >  0) {
                return i + 'a';
            }
        }
        return 0;
    }
};
