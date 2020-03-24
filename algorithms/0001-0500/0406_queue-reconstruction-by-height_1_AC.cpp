// Naive solution
#include <algorithm>
#include <utility>
using std::make_pair;
using std::sort;

typedef pair<int, int> PII;

bool comparator(const PII &p1, const PII &p2)
{
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    if (p1.second != p2.second) {
        return p1.second > p2.second;
    }
    return true;
}

class Solution {
public:
    vector<PII> reconstructQueue(vector<PII>& people) {
        int n = people.size();
        vector<PII> res(n, make_pair(-1, -1));
        sort(people.begin(), people.end(), comparator);
        int i, j;
        int cnt;
        for (i = 0; i < n; ++i) {
            cnt = 0;
            for (j = 0; j < n; ++j) {
                if (res[j].first >= 0) {
                    // Occupied
                    continue;
                }
                ++cnt;
                if (cnt > people[i].second) {
                    break;
                }
            }
            res[j] = people[i];
        }
        return res;
    }
};
