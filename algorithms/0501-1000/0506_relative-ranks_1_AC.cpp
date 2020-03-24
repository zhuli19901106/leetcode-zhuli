#include <algorithm>
#include <string>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::sort;
using std::string;
using std::to_string;
using std::vector;

typedef pair<int, int> PII;
bool comparator(const PII &p1, const PII &p2)
{
    return p1.first > p2.first;
}

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<string> res;
        vector<pair<int, int>> v;
        static const string title[3] = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(make_pair(nums[i], i));
        }
        sort(v.begin(), v.end(), comparator);
        
        res.resize(n);
        for (i = 0; i < n; ++i) {
            if (i < 3) {
                res[v[i].second] = title[i];
            } else {
                res[v[i].second] = to_string(i + 1);
            }
        }
        v.clear();
        
        return res;
    }
};
