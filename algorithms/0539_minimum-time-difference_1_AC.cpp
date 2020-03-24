#include <algorithm>
#include <cstdio>
#include <vector>
using std::min;
using std::sscanf;
using std::vector;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int h, m;
        vector<int> v;
        for (string &s: timePoints) {
            sscanf(s.data(), "%d:%d", &h, &m);
            v.push_back(h * 60 + m);
        }
        sort(v.begin(), v.end());
        
        int n = v.size();
        int i;
        int res = v[1] - v[0];
        for (i = 0; i + 1 < n; ++i) {
            res = min(res, v[i + 1] - v[i]);
        }
        res = min(res, v[0] + 1440 - v[n - 1]);
        
        return res;
    }
};
