/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

bool comparator(const Interval &x, const Interval &y) {
    if (x.start != y.start) {
        return x.start < y.start;
    }
    if (x.end != y.end) {
        return x.end < y.end;
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
            if (a[i].end > a[i + 1].start) {
                return false;
            }
        }
        return true;
    }
};
