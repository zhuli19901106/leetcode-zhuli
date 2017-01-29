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
using std::max;
using std::min;
using std::sort;

bool comparator(const Interval &i1, const Interval &i2)
{
    if (i1.start != i2.start) {
        return i1.start < i2.start;
    }
    if (i1.end != i2.end) {
        return i1.end < i2.end;
    }
    return false;
}

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        auto &a = intervals;
        int n = a.size();
        Interval it;
        
        sort(a.begin(), a.end(), comparator);
        
        int i, j;
        i = 0;
        while (i < n) {
            it = a[i];
            j = i + 1;
            while (j < n && it.end >= a[j].start) {
                it.end = max(it.end, a[j].end);
                ++j;
            }
            res.push_back(it);
            i = j;
        }
        return res;
    }
};
