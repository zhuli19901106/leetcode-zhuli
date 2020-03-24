#include <utility>
using std::make_pair;
using std::pair;

typedef pair<string, string> PSS;

bool comparator(const PSS &p1, const PSS &p2)
{
    return p1.second < p2.second;
}

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        int n = strs.size();
        if (n == 0) {
            return res;
        }
        vector<PSS> v;
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(make_pair(strs[i], strs[i]));
            sort(v[i].second.begin(), v[i].second.end());
        }
        sort(v.begin(), v.end(), comparator);
        
        int j;
        i = 0;
        while (i < n) {
            res.push_back(vector<string>());
            j = i;
            while (j < n && v[j].second == v[i].second) {
                res.back().push_back(v[j].first);
                ++j;
            }
            i = j;
        }
        v.clear();
        return res;
    }
};
