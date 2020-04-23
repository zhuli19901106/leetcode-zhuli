// https://leetcode.com/explore/interview/card/apple/346/sorting-and-searching/2026/
#include <algorithm>
using std::max;
using std::min;
using std::sort;

typedef vector<int> VI;

bool comparator(const VI &i1, const VI &i2)
{
    if (i1[0] != i2[0]) {
        return i1[0] < i2[0];
    }
    if (i1[1] != i2[1]) {
        return i1[1] < i2[1];
    }
    return false;
}

class Solution {
public:
    vector<VI> merge(vector<VI>& VIs) {
        vector<VI> res;
        auto &a = VIs;
        int n = a.size();
        VI it;
        
        sort(a.begin(), a.end(), comparator);
        
        int i, j;
        i = 0;
        while (i < n) {
            it = a[i];
            j = i + 1;
            while (j < n && it[1] >= a[j][0]) {
                it[1] = max(it[1], a[j][1]);
                ++j;
            }
            res.push_back(it);
            i = j;
        }
        return res;
    }
};
