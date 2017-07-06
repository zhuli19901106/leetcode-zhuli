#include <algorithm>
#include <queue>
#include <vector>
using std::priority_queue;
using std::sort;
using std::vector;

bool comparator(const vector<int> &v1, const vector<int> &v2)
{
    return v1[1] < v2[1];
}

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        auto &vc = courses;
        sort(vc.begin(), vc.end(), comparator);
        
        priority_queue<int> pq;
        int now = 0;
        int tp;
        for (auto &c: vc) {
            if (now + c[0] <= c[1]) {
                now += c[0];
                pq.push(c[0]);
                continue;
            }
            
            tp = pq.top();
            if (c[0] >= tp) {
                continue;
            }
            
            now += c[0] - tp;
            pq.pop();
            pq.push(c[0]);
        }
        
        int res = pq.size();
        return res;
    }
};
