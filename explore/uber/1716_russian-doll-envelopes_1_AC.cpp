// LIS
#include <algorithm>
#include <utility>
#include <vector>
using std::lower_bound;
using std::max;
using std::pair;
using std::sort;
using std::vector;

typedef vector<int> VI;
bool comparator(const VI &p1, const VI &p2)
{
    if (p1[0] != p2[0]) {
        return p1[0] < p2[0];
    }
    if (p1[1] != p2[1]) {
        return p1[1] > p2[1];
    }
    return false;
}

class Solution {
public:
    int maxEnvelopes(vector<VI>& envelopes) {
        auto &a = envelopes;
        int n = a.size();
        sort(a.begin(), a.end(), comparator);
        
        vector<int> v;
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(a[i][1]);
        }
        
        int res = LIS(v);
        v.clear();
        
        return res;
    }
private:
    int LIS(vector<int> &v) {
        int n = v.size();
        if (n < 2) {
            return n;
        }
        
        vector<int> seq;
        int i, j;
        
        seq.push_back(v[0]);
        for (i = 1; i < n; ++i) {
            if (v[i] > seq.back()) {
                seq.push_back(v[i]);
            }
            j = lower_bound(seq.begin(), seq.end(), v[i]) - seq.begin();
            seq[j] = v[i];
        }
        int res = seq.size();
        seq.clear();
        
        return res;
    }
};
