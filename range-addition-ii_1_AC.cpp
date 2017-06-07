// Brainteaser
#include <algorithm>
#include <vector>
using std::min;
using std::vector;

class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int rm, rn;
        
        rm = m;
        rn = n;
        for (auto &op: ops) {
            if (op[0] == 0 || op[1] == 0) {
                continue;
            }
            rm = min(rm, op[0]);
            rn = min(rn, op[1]);
        }
        return rm * rn;
    }
};
