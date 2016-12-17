#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, string> m1;
        unordered_map<string, char> m2;
        unordered_map<char, string>::iterator it1;
        unordered_map<string, char>::iterator it2;
        vector<string> v;
        
        splitString(str, v);
        if (pattern.size() != v.size()) {
            return false;
        }
        int n = pattern.size();
        int i;
        for (i = 0; i < n; ++i) {
            it1 = m1.find(pattern[i]);
            it2 = m2.find(v[i]);
            if (it1 == m1.end() && it2 == m2.end()) {
                m1[pattern[i]] = v[i];
                m2[v[i]] = pattern[i];
            }else if (it1 != m1.end() && it2 != m2.end()) {
                if (it1->first != pattern[i] || it2->first != v[i]) {
                    break;
                }
            } else {
                break;
            }
        }
        m1.clear();
        m2.clear();
        v.clear();
        return i == n;
    }
private:
    void splitString(string s, vector<string> &v) {
        string w = "";
        int n = s.size();
        int i, j;
        
        i = 0;
        while (i < n) {
            j = i;
            while (j < n && s[j] != ' ') {
                w.push_back(s[j++]);
            }
            v.push_back(w);
            w.clear();
            i = j + 1;
        }
    }
};
