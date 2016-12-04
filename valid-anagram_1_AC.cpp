// Use a counter array with fixed size.
#include <cstring>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        // Only lowercase letters.
        const int DICT_SIZE = 26;
        int cnt[DICT_SIZE];
        
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        int i;
        int n = s.size();
        for (i = 0; i < n; ++i) {
            ++cnt[s[i] - 'a'];
            --cnt[t[i] - 'a'];
        }
        for (i = 0; i < DICT_SIZE; ++i) {
            if (cnt[i] != 0) {
                return false;
            }
        }
        return true;
    }
};
