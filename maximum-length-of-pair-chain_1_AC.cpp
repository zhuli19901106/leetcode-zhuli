// Think for a while before coding.
#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

typedef vector<int> VI;

bool comparator(const VI &v1, const VI &v2)
{
    if (v1[1] != v2[1]) {
        return v1[1] < v2[1];
    }
    return false;
}

class Solution {
public:
    int findLongestChain(vector<VI> &pairs) {
        auto &v = pairs;
        int n = v.size();
        int i;
        
        sort(v.begin(), v.end(), comparator);
        int max_val = v[0][1];
        int max_len = 1;
        for (i = 1; i < n; ++i) {
            // the key
            if (v[i][0] > max_val) {
                max_val = v[i][1];
                ++max_len;
            }
        }
        return max_len;
    }
};
