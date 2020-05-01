// KMP algorithm
#include <vector>
using std::vector;

class Solution {
public:
    int strStr(string haystack, string needle) {
        string &str = haystack;
        string &pat = needle;
        int ls = str.size();
        int lp = pat.size();
        if (ls < lp) {
            return -1;
        }
        if (lp == 0) {
            // Empty pattern is always considered a match.
            return 0;
        }
        vector<int> next;
        next.resize(lp + 1);
        getNextArray(pat, next);
        int res = KMPMatch(str, pat, next);
        next.clear();
        
        return res;
    }
private:
    void getNextArray(string &pat, vector<int> &next) {
        int lp = pat.size();
        int i = 0;
        int j = -1;
        
        next[i] = j;
        while (i < lp) {
            if (j == -1 || pat[i] == pat[j]) {
                next[++i] = ++j;
            } else {
                j = next[j];
            }
        }
    }
    
    int KMPMatch(string &str, string &pat, vector<int> &next) {
        int ls = str.size();
        int lp = pat.size();
        int i = 0;
        int j = 0;
        while (i < ls) {
            if (j == -1 || str[i] == pat[j]) {
                ++i;
                ++j;
            } else {
                j = next[j];
            }
            if (j == lp) {
                return i - lp;
            }
        }
        return -1;
    }
};
