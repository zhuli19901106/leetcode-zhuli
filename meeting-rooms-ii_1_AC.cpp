// Think it through before you start coding, that saves lots of lines.
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
#include <functional>
#include <queue>
#include <vector>
using std::greater;
using std::max;
using std::priority_queue;
using std::sort;
using std::vector;

bool comparator(Interval &x, Interval &y)
{
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
    int minMeetingRooms(vector<Interval>& intervals) {
        auto &a = intervals;
        int n = a.size();
        sort(a.begin(), a.end(), comparator);
        
        priority_queue<int, vector<int>, greater<int>> pq;
        int res = 0;
        int i;
        for (i = 0; i < n; ++i) {
            while (!pq.empty() && pq.top() <= a[i].start) {
                pq.pop();
            }
            pq.push(a[i].end);
            res = max(res, (int)pq.size());
        }
        while (!pq.empty()) {
            pq.pop();
        }
        
        return res;
    }
};
