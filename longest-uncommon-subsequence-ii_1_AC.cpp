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
    int findLUSlength(vector<string>& strs) {
        auto &a = strs;
        sort(a.begin(), a.end(), comparator);
        
        int n = a.size();
        int i, j;
        vector<bool> vb(n, false);
        for (i = 0; i < n; ++i) {
            for (j = i + 1; j < n; ++j) {
                vb[j] = (vb[j] || isSubseq(a[i], a[j]));
            }
        }
        for (i = 0; i + 1 < n; ++i) {
            if (a[i] == a[i + 1]) {
                vb[i] = vb[i + 1];
            }
        }
        
        int res = -1;
        for (i = 0; i < n; ++i) {
            if (!vb[i]) {
                res = a[i].size();
                break;
            }
        }
        vb.clear();
        
        return res;
    }
private:
    bool isSubseq(const string &s1, const string &s2) {
        // Check if s2 is a subsequence of s1.
        int l1 = s1.size();
        int l2 = s2.size();
        
        if (l1 < l2) {
            return false;
        }
        
        int i, j;
        i = j = 0;
        while (i < l1 && j < l2) {
            if (s1[i] == s2[j]) {
                ++j;
            }
            ++i;
        }
        return j == l2;
    }
};
