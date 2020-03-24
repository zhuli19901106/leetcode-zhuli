#include <vector>
using std::vector;

class Solution {
public:
    string simplifyPath(string path) {
        string s = "";
        vector<string> v;
        
        int lp = path.size();
        int i, j;
        
        i = 0;
        while (i < lp) {
            j = i + 1;
            s.clear();
            while (j < lp && path[j] != '/') {
                s.push_back(path[j++]);
            }
            i = j;
            if (s == "" || s == ".") {
                continue;
            }
            if (s == "..") {
                if (v.size() > 0) {
                    v.pop_back();
                }
                continue;
            }
            v.push_back(s);
        }
        
        string res = "";
        int n = v.size();
        for (i = 0; i < n; ++i) {
            res.push_back('/');
            res += v[i];
        }
        v.clear();
        if (res == "") {
            res.push_back('/');
        }
        return res;
    }
};
