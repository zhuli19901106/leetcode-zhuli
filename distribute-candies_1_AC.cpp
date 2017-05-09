#include <algorithm>
#include <unordered_set>
using std::min;
using std::unordered_set;

class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> us;
        for (auto &c: candies) {
            us.insert(c);
        }
        int res = min(us.size(), candies.size() / 2);
        us.clear();
        
        return res;
    }
};
