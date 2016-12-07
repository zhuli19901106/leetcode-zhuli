#include <unordered_map>
using std::unordered_map;

typedef long long int int64;
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        unordered_map<int64, int> um;
        int n = points.size();
        int i, j;
        unordered_map<int64, int>::const_iterator it;
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                ++um[dist(points[i], points[j])];
            }
            for (it = um.begin(); it != um.end(); ++it) {
                res += it->second * (it->second - 1);
            }
            um.clear();
        }
        return res;
    }
private:
    int64 dist(pair<int, int>& p1, pair<int, int>& p2) {
        return 1LL * (p1.first - p2.first) * (p1.first - p2.first) + 
               1LL * (p1.second - p2.second) * (p1.second - p2.second);
    }
};
