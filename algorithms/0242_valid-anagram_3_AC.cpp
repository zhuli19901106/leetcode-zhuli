#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> cnt;
        int n = s.size();
        int i;
        for (i = 0; i < n; ++i) {
            ++cnt[s[i]];
            --cnt[t[i]];
        }
        unordered_map<char, int>::const_iterator it;
        for (it = cnt.begin(); it != cnt.end(); ++it) {
            if (it->second != 0) {
                return false;
            }
        }
        cnt.clear();
        return true;
    }
};
