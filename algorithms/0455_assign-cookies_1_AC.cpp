#include <algorithm>
using std::sort;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int ng = g.size();
        int ns = s.size();
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int i = 0;
        int j = 0;
        while (i < ns && j < ng) {
            if (s[i] >= g[j]) {
                ++j;
            }
            ++i;
        }
        return j;
    }
};
