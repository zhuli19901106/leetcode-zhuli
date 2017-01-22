#include <cmath>
using std::sqrt;

class Solution {
public:
    vector<int> constructRectangle(int area) {
        int rt = sqrt(area);
        while (rt > 1 && area % rt != 0) {
            --rt;
        }
        vector<int> res;
        res.push_back(area / rt);
        res.push_back(rt);
        return res;
    }
};
