#include <algorithm>
#include <unordered_map>
#include <vector>
using std::max;
using std::unordered_map;
using std::vector;

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> um;
        int sum;
        for (vector<int> &v: wall) {
            sum = 0;
            for (int &val: v) {
                sum += val;
                ++um[sum];
            }
            um.erase(sum);
        }
        
        int h = 0;
        for (auto &p: um) {
            h = max(h, p.second);
        }
        h = wall.size() - h;
        um.clear();
        
        return h;
    }
};
