// Cross product can be used to calculate area.
#include <vector>
using std::vector;

class Solution {
public:
    bool isConvex(vector<vector<int>>& points) {
        auto &v = points;
        int n = v.size();
        int i;
        
        int a1, a2;
        vector<int> v1(2), v2(2);
        
        a1 = 0;
        for (i = 0; i < n; ++i) {
            a2 = (v[(i + 1) % n][0] - v[i][0]) * (v[(i + 2) % n][1] - v[i][1]) 
                - (v[(i + 2) % n][0] - v[i][0]) * (v[(i + 1) % n][1] - v[i][1]);
            if (a2 == 0) {
                // Skip the zeroes, think about it.
                continue;
            }
            if (sign(a1) * sign(a2) == -1) {
                return false;
            }
            a1 = a2;
        }
        return true;
    }
private:
    int sign(int x) {
        return x > 0 ? +1 : x < 0 ? -1 : 0;
    }
};
