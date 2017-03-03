#include <algorithm>
#include <string>
#include <vector>
using std::sort;
using std::string;
using std::vector;

bool comparator(const string &s1, const string &s2)
{
    if (s1.size() != s2.size()) {
        return s1.size() > s2.size();
    }
    return s1 < s2;
}

class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), comparator);
        
        int n = d.size();
        if (n == 0) {
            return "";
        }
        
        vector<int> idx(n, 0);
        string res = "";
        int ls = s.size();
        
        int i, j;
        for (i = 0; i < ls; ++i) {
            for (j = 0; j < n; ++j) {
                if (idx[j] == d[j].size()) {
                    continue;
                }
                if (s[i] == d[j][idx[j]]) {
                    ++idx[j];
                }
            }
        }
        for (i = 0; i < n; ++i) {
            if (idx[i] == d[i].size()) {
                res = d[i];
                break;
            }
        }
        idx.clear();
        return res;
    }
};
