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

typedef struct Tuple {
    int x;
    int y;
    int idx;
    
    Tuple() {}
    Tuple(int _x, int _y, int _idx): x(_x), y(_y), idx(_idx) {}
} Tuple;

bool comparator(const Tuple &t1, const Tuple &t2)
{
    if (t1.x != t2.x) {
        return t1.x < t2.x;
    }
    if (t1.y != t2.y) {
        return t1.y < t2.y;
    }
    if (t1.idx != t2.idx) {
        return t1.idx < t2.idx;
    }
    return true;
}

class Solution {
public:
    vector<int> findRightInterval(vector<Interval>& intervals) {
        int n = intervals.size();
        int i;
        vector<Tuple> v;
        for (i = 0; i < n; ++i) {
            v.push_back(Tuple(intervals[i].start, intervals[i].end, i));
        }
        sort(v.begin(), v.end(), comparator);
        
        // Binary search here
        vector<int> res(n, -1);
        int ll, mm, rr;
        for (i = 0; i < n - 1; ++i) {
            ll = i + 1;
            rr = n - 1;
            if (v[i].y <= v[ll].x) {
                res[v[i].idx] = v[ll].idx;
                continue;
            }
            if (v[i].y > v[rr].x) {
                continue;
            }
            while (rr - ll > 1) {
                mm = ll + (rr - ll >> 1);
                if (v[i].y <= v[mm].x) {
                    rr = mm;
                } else {
                    ll = mm;
                }
            }
            res[v[i].idx] = v[rr].idx;
        }
        v.clear();
        return res;
    }
};
