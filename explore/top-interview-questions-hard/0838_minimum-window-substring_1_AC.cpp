#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    string minWindow(string s, string t) {
        static const int DICT_SIZE = 256;
        
        int ls = s.size();
        int lt = t.size();
        
        if (lt == 0 || ls < lt) {
            return "";
        }
        
        int cnt = 0;
        vector<int> vs(DICT_SIZE, 0), vt(DICT_SIZE, 0);
        int i;
        for (i = 0; i< lt; ++i) {
            ++vt[t[i]];
            ++cnt;
        }
        
        int min_len = ls + 1;
        string res = "";
        char ch;
        
        int j;
        j = 0;
        for (i = 0; i < ls; ++i) {
            if (vs[s[i]] < vt[s[i]]) {
                --cnt;
            }
            ++vs[s[i]];
            if (cnt > 0) {
                continue;
            }
            
            do {
                ch = s[j++];
                --vs[ch];
            } while (vs[ch] >= vt[ch]);
            ++cnt;
            
            if (i - j + 2 < min_len) {
                min_len = i - j + 2;
                res = s.substr(j - 1, min_len);
            }
        }
        
        return res;
    }
};
