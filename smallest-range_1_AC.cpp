#include <algorithm>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::sort;
using std::vector;

typedef pair<int, int> PII;
bool comparator(const PII &p1, const PII &p2)
{
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    if (p1.second != p2.second) {
        return p1.second < p2.second;
    }
    return false;
}

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<pair<int, int>> v;
        int nl = nums.size();
        int i;
        int len;
        for (i = 0; i < nl; ++i) {
            for (auto &x: nums[i]) {
                v.push_back(make_pair(x, i));
            }
        }
        sort(v.begin(), v.end(), comparator);
        
        vector<int> c(nl, 0);
        int cc = 0;
        int mi, mj;
        int j;
        int r, min_r;
        int idx;
        
        len = v.size();
        mi = 0;
        mj = len - 1;
        min_r = v[mj].first - v[mi].first;
        i = 0;
        j = 0;
        do {
            while (j < len && cc < nl) {
                // push j forward until every list is covered
                idx = v[j].second;
                if (c[idx] == 0) {
                    ++cc;
                }
                ++c[idx];
                ++j;
            }
            while (cc >= nl) {
                // push i forward until not every list is covered
                idx = v[i].second;
                --c[idx];
                ++i;
                if (c[idx] == 0) {
                    --cc;
                }
            }
            r = v[j - 1].first - v[i - 1].first;
            if (r < min_r) {
                mi = i - 1;
                mj = j - 1;
                min_r = r;
            }
        } while (j < len);
        
        vector<int> res(2);
        res[0] = v[mi].first;
        res[1] = v[mj].first;
        v.clear();
        c.clear();
        
        return res;
    }
};
