// For small DICT_SIZE as 26, heap optimization is hardly efficient.
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    string rearrangeString(string s, int k) {
        if (k < 2) {
            return s;
        }
        
        static const int DICT_SIZE = 26;
        vector<int> c(DICT_SIZE, 0);
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            ++c[s[i] - 'a'];
        }
        
        // Cool down
        vector<bool> cd(DICT_SIZE, false);
        string res = "";
        int j;
        int mi;
        for (i = 0; i < ls; ++i) {
            if (i - k >= 0) {
                cd[res[i - k] - 'a'] = false;
            }
            
            mi = -1;
            for (j = 0; j < DICT_SIZE; ++j) {
                if (c[j] == 0 || cd[j]) {
                    continue;
                }
                if (mi == -1 || c[j] > c[mi]) {
                    mi = j;
                }
            }
            if (mi == -1) {
                break;
            }
            res.push_back('a' + mi);
            --c[mi];
            cd[mi] = true;
        }
        if (res.size() < ls) {
            res = "";
        }
        c.clear();
        cd.clear();
        
        return res;
    }
};
