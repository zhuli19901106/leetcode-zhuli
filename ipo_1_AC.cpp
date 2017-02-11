// Why is problem rated "hard"?
#include <queue>
#include <utility>
using std::make_pair;
using std::pair;
using std::priority_queue;

typedef pair<int, int> PII;
bool comparator(const PII &p1, const PII &p2)
{
    return p1.second < p2.second;
}

class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        vector<pair<int, int>> v;
        int n = Profits.size();
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(make_pair(Profits[i], Capital[i]));
        }
        sort(v.begin(), v.end(), comparator);
        
        priority_queue<int> pq;
        int j;
        i = 0;
        j = 0;
        while (true) {
            while (i < n && v[i].second <= W) {
                pq.push(v[i++].first);
            }
            if (pq.empty()) {
                break;
            }
            
            if (j < k && !pq.empty()) {
                W += pq.top();
                pq.pop();
                ++j;
            }
            if (j >= k) {
                break;
            }
        }
        
        while (!pq.empty()) {
            pq.pop();
        }
        
        return W;
    }
};
