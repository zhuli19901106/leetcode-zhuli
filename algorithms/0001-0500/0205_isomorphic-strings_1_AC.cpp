// Bidirection mapping is a good way for fast lookup.
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        unordered_map<char, char> m1, m2;
        unordered_map<char, char>::iterator i1, i2;
        int n = s.size();
        int i;
        for (i = 0; i < n; ++i) {
            i1 = m1.find(s[i]);
            i2 = m2.find(t[i]);
            if (i1 == m1.end() && i2 == m2.end()) {
                m1[s[i]] = t[i];
                m2[t[i]] = s[i];
            } else if (i1 != m1.end() && i2 != m2.end()) {
                if (i1->second != t[i] || i2->second != s[i]) {
                    break;
                }
            } else {
                break;
            }
        }
        m1.clear();
        m2.clear();
        return i == n;
    }
};
