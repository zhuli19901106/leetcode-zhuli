// The API has changed since I last did this
#include <algorithm>
#include <functional>
#include <queue>
#include <vector>
using std::greater;
using std::max;
using std::priority_queue;
using std::sort;
using std::vector;

typedef vector<int> VI;

bool comparator(VI &x, VI &y)
{
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
    int minMeetingRooms(vector<VI>& intervals) {
        auto &a = intervals;
        int n = a.size();
        sort(a.begin(), a.end(), comparator);
        
        priority_queue<int, vector<int>, greater<int>> pq;
        int res = 0;
        int i;
        for (i = 0; i < n; ++i) {
            while (!pq.empty() && pq.top() <= a[i][0]) {
                pq.pop();
            }
            pq.push(a[i][1]);
            res = max(res, (int)pq.size());
        }
        while (!pq.empty()) {
            pq.pop();
        }
        
        return res;
    }
};
