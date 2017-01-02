// O(n ^ 2) DP solution
#include <algorithm>
using std::max;
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
        vector<int> dp(n, 1);
        int res = 0;
        
        int i, j;
        sort(a.begin(), a.end(), comparator);
        for (i = n - 1; i >= 0; --i) {
            j = n - 1;
            while (j > i && a[i].end <= a[j].start) {
                dp[i] = max(dp[i], dp[j] + 1);
                --j;
            }
            res = max(res, dp[i]);
        }
        dp.clear();
        return n - res;
    }
};
