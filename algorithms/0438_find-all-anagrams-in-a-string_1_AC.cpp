#include <cstring>
using std::memset;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        
        int ls = s.size();
        int lp = p.size();
        if (ls < lp) {
            return res;
        }
        
        int i;
        diff = 0;
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        for (i = 0; i < lp; ++i) {
            --cnt[p[i] - 'a'];
            ++diff;
        }
        i = 0;
        while (i < lp) {
            addChar(s, i);
            ++i;
            if (diff == 0) {
                res.push_back(i - lp);
            }
        }
        while (i < ls) {
            addChar(s, i);
            removeChar(s, i - lp);
            ++i;
            if (diff == 0) {
                res.push_back(i - lp);
            }
        }
        return res;
    }
private:
    static const int DICT_SIZE = 26;
    int cnt[DICT_SIZE];
    int diff;
    
    // Whenever you have to write a piece of code more than once, encapsulate it.
    void addChar(string &s, int pos) {
        ++cnt[s[pos] - 'a'];
        if (cnt[s[pos] - 'a'] > 0) {
            ++diff;
        } else {
            --diff;
        }
    }
    
    void removeChar(string &s, int pos) {
        --cnt[s[pos] - 'a'];
        if (cnt[s[pos] - 'a'] < 0) {
            ++diff;
        } else {
            --diff;
        }
    }
};
