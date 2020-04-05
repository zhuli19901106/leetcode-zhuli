// So why is this problem rated "Hard" anyway?
// You can see the difficulty inflation in those interview questions these days.
// Back in the old days, problems used to be easy.
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

typedef vector<int> VI;

class Solution {
public:
    vector<VI> insert(vector<VI>& VIs, VI& newVI) {
        auto &a = VIs;
        auto &ni = newVI;
        vector<VI> res;
        
        int n = a.size();
        int i = 0;
        while (i < n && a[i][1] < ni[0]) {
            res.push_back(a[i++]);
        }
        while (i < n) {
            if (a[i][0] > ni[1]) {
                break;
            }
            ni[0] = min(ni[0], a[i][0]);
            ni[1] = max(ni[1], a[i][1]);
            ++i;
        }
        res.push_back(ni);
        while (i < n && a[i][0] > ni[1]) {
            res.push_back(a[i++]);
        }
        
        return res;
    }
};
