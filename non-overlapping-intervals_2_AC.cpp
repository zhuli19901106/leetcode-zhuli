// Why DP when it's time to be greedy?
#include <algorithm>
using std::sort;
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
bool comparator(const Interval &i1, const Interval &i2)
{
    if (i1.start != i2.start) {
        return i1.start < i2.start;
    }
    if (i1.end != i2.end) {
        return i1.end < i2.end;
    }
    return true;
}

class Solution {
public:
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        vector<Interval> &a = intervals;
        int n = a.size();
        if (n == 0) {
            return 0;
        }
        int res = 1;
        int i;
        int idx = n - 1;
        
        sort(a.begin(), a.end(), comparator);
        for (i = n - 2; i >= 0; --i) {
            if (a[i].end <= a[idx].start) {
                ++res;
                idx = i;
            }
        }
        return n - res;
    }
};
