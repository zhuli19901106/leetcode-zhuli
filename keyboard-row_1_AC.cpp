#include <cctype>
using std::isupper;
using std::tolower;

class Solution {
public:
    Solution() {
        vector<string> v;
        v.push_back("qwertyuiop");
        v.push_back("QWERTYUIOP");
        v.push_back("asdfghjkl");
        v.push_back("ASDFGHJKL");
        v.push_back("zxcvbnm");
        v.push_back("ZXCVBNM");
        pos.resize(256, -1);
        
        int n = v.size();
        int i, j;
        int ls;
        for (i = 0; i < n; ++i) {
            ls = v[i].size();
            for (j = 0; j < ls; ++j) {
                pos[v[i][j]] = i / 2;
            }
        }
    }
    
    vector<string> findWords(vector<string>& words) {
        vector<string> res;
        int n = words.size();
        int ls;
        int i, j;
        int p;
        for (i = 0; i < n; ++i) {
            ls = words[i].size();
            if (ls == 0) {
                continue;
            }
            p = pos[words[i][0]];
            for (j = 1; j < ls; ++j) {
                if (pos[words[i][j]] != p) {
                    break;
                }
            }
            if (j == ls) {
                res.push_back(words[i]);
            }
        }
        
        return res;
    }
    
    ~Solution() {
        pos.clear();
    }
private:
    vector<int> pos;
};
