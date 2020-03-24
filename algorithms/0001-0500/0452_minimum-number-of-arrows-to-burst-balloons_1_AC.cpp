#include <algorithm>
using std::min;
using std::sort;

typedef pair<int, int> PII;

bool compatator(const PII &p1, const PII &p2)
{
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    if (p1.second != p2.second) {
        return p1.second < p2.second;
    }
    return true;
}

class Solution {
public:
    int findMinArrowShots(vector<PII>& points) {
        int n = points.size();
        if (n == 0) {
            return 0;
        }
        
        int res = 1;
        int i;
        sort(points.begin(), points.end(), compatator);
        for (i = 1; i < n; ++i) {
            if (points[i].first > points[i - 1].second) {
                ++res;
            } else {
                points[i].second = min(points[i - 1].second, points[i].second);
            }
        }
        return res;
    }
};
