// It's DP, but the array is represented using hash map.
#include <climits>
#include <cstdint>
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        vector<unordered_map<int, int>> um(n);
        int res = 0;
        int64_t d;
        
        int cc;
        int i, j;
        bool found;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < i; ++j) {
                d = (int64_t)A[i] - A[j];
                if (d < INT_MIN || d > INT_MAX) {
                    continue;
                }
                found = (um[j].find(d) != um[j].end());
                // Avoid MLE here
                cc = found ? um[j][d] : 0;
                res += cc;
                um[i][d] += cc + 1;
            }
        }
        um.clear();
        
        return res;
    }
};
