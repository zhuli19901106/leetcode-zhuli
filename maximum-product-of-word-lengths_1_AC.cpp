// Can this problem be solved under O(n^2)?
#include <algorithm>
#include <vector>
#include <utility>
using std::make_pair;
using std::max;
using std::pair;
using std::vector;

class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size();
        int i, j;
        vector<pair<int, int>> v;
        for (i = 0; i < n; ++i) {
            v.push_back(make_pair(getBitmask(words[i]), words[i].size()));
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = i + 1; j < n; ++j) {
                if ((v[i].first & v[j].first) != 0) {
                    continue;
                }
                res = max(res, v[i].second * v[j].second);
            }
        }
        v.clear();
        
        return res;
    }
private:
    int getBitmask(const string &s) {
        // Suppose only lower case letters here
        int n = s.size();
        int i;
        int mask = 0;
        for (i = 0; i < n; ++i) {
            mask |= 1 << s[i] - 'a';
        }
        return mask;
    }
};
