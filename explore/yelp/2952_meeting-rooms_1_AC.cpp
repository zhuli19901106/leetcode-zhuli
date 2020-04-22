#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

typedef vector<int> Interval;
bool comparator(const Interval &x, const Interval &y) {
    if (x[0] != y[0]) {
        return x[0] < y[0];
    }
    if (x[1] != y[1]) {
        return x[1] < y[1];
    }
    return false;
}

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        auto &a = intervals;
        sort(a.begin(), a.end(), comparator);
        
        int n = a.size();
        int i;
        for (i = 0; i + 1 < n; ++i) {
            if (a[i][1] > a[i + 1][0]) {
                return false;
            }
        }
        return true;
    }
};
