// So why is this problem rated "Hard" anyway?
// You can see the difficulty inflation in those interview questions these days.
// Back in the old days, problems used to be easy.
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
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        auto &a = intervals;
        auto &ni = newInterval;
        vector<Interval> res;
        
        int n = a.size();
        int i = 0;
        while (i < n && a[i].end < ni.start) {
            res.push_back(a[i++]);
        }
        while (i < n) {
            if (a[i].start > ni.end) {
                break;
            }
            ni.start = min(ni.start, a[i].start);
            ni.end = max(ni.end, a[i].end);
            ++i;
        }
        res.push_back(ni);
        while (i < n && a[i].start > ni.end) {
            res.push_back(a[i++]);
        }
        
        return res;
    }
};
