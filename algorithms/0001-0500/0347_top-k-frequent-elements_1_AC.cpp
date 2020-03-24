#include <algorithm>
#include <unordered_map>
#include <utility>
using std::make_pair;
using std::pair;
using std::sort;
using std::unordered_map;

typedef pair<int, int> PII;
typedef unordered_map<int, int> UMII;

bool comparator(const PII &p1, const PII &p2)
{
    if (p1.second != p2.second) {
        return p1.second > p2.second;
    }
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    return true;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        UMII um;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            ++um[nums[i]];
        }
        
        UMII::const_iterator it;
        vector<PII> v;
        for (it = um.begin(); it != um.end(); ++it) {
            v.push_back(make_pair(it->first, it->second));
        }
        sort(v.begin(), v.end(), comparator);
        um.clear();
        
        n = v.size();
        vector<int> res;
        for (i = 0; i < k; ++i) {
            res.push_back(v[i].first);
        }
        v.clear();
        
        return res;
    }
};
