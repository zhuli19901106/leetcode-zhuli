// 1AC, sort it out.
#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using std::max;
using std::sort;
using std::string;
using std::to_string;
using std::vector;

bool comparator(const string &s1, const string &s2)
{
    if (s1.size() != s2.size()) {
        return s1.size() < s2.size();
    }
    if (s1.back() != s2.back()) {
        return s1.back() < s2.back();
    }
    return s1 < s2;
}

class Solution {
public:
    vector<string> wordsAbbreviation(vector<string>& dict) {
        auto &d = dict;
        
        unordered_map<string, int> um;
        int n = d.size();
        int i;
        for (i = 0; i < n; ++i) {
            um[d[i]] = i;
        }
        
        auto a = d;
        sort(a.begin(), a.end(), comparator);
        
        vector<int> plen(n, 1);
        int j;
        int len;
        for (i = 0; i + 1 < n; ++i) {
            if (a[i].size() <= 2) {
                continue;
            }
            if (a[i].size() != a[i + 1].size()) {
                continue;
            }
            if (a[i].back() != a[i + 1].back()) {
                continue;
            }
            len = a[i].size();
            for (j = 0; j < len; ++j) {
                if (a[i][j] != a[i + 1][j]) {
                    break;
                }
            }
            plen[i] = max(plen[i], j + 1);
            plen[i + 1] = max(plen[i + 1], j + 1);
        }
        
        vector<string> res(n);
        for (i = 0; i < n; ++i) {
            j = um[a[i]];
            len = a[i].size() - plen[i] - 1;
            if (a[i].size() <= 2 || len <= 1) {
                res[j] = a[i];
            } else {
                res[j] = a[i].substr(0, plen[i]) + to_string(len) + a[i].back();
            }
        }
        a.clear();
        um.clear();
        
        return res;
    }
};
