#include <algorithm>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::sort;
using std::vector;

typedef pair<int, int> PII;
bool comparator(const PII &p1, const PII &p2)
{
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    if (p1.second != p2.second) {
        return p1.second < p2.second;
    }
    return false;
}

class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        auto &a = nums;
        int n = a.size();
        
        vector<PII> v;
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(make_pair(a[i], i));
        }
        sort(v.begin(), v.end(), comparator);
        
        int j, k;
        int res = 0;
        int sum;
        for (i = 0; i < n - 2; ++i) {
            k = n - 1;
            for (j = i + 1; j < k && j < n - 1; ++j) {
                while (j < k) {
                    sum = v[i].first + v[j].first + v[k].first;
                    if (sum < target) {
                        break;
                    }
                    --k;
                }
                res += k - j;
            }
        }
        v.clear();
        
        return res;
    }
};
