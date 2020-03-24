#include <cstring>
using std::memset;

class Solution {
public:
    int firstUniqChar(string s) {
        // Only lowercase letters.
        const int DICT_SIZE = 26;
        int idx[DICT_SIZE];
        memset(idx, -1, DICT_SIZE * sizeof(int));
        
        int i;
        int n = s.size();
        const int DUP = -2; // For "duplicated".
        for (i = 0; i < n; ++i) {
            if (idx[s[i] - 'a'] == -1) {
                idx[s[i] - 'a'] = i;
            } else {
                idx[s[i] - 'a'] = DUP;
            }
        }
        int res = -1;
        for (i = 0; i < DICT_SIZE; ++i) {
            if (idx[i] < 0) {
                continue;
            }
            if (res == -1 || res > idx[i]) {
                res = idx[i];
            }
        }
        return res;
    }
};
