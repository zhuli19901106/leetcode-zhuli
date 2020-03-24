#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        unordered_map<int, int> um;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            ++um[nums[i]];
        }
        
        vector<int> v, c;
        for (auto it = um.begin(); it != um.end(); ++it) {
            v.push_back(it->first);
            c.push_back(it->second);
        }
        um.clear();
        
        vector<vector<int>> res;
        vector<int> vc;
        dfs(vc, v, c, res);
        v.clear();
        c.clear();
        return res;
    }
private:
    void dfs(vector<int> &vc, vector<int> &v, vector<int> &c, vector<vector<int>> &res) {
        if (vc.size() == c.size()) {
            vector<int> nums;
            int i, j;
            for (i = 0; i < vc.size(); ++i) {
                for (j = 0; j < vc[i]; ++j) {
                    nums.push_back(v[i]);
                }
            }
            res.push_back(nums);
            return;
        }
        
        int idx = vc.size();
        int i;
        for (i = 0; i <= c[idx]; ++i) {
            vc.push_back(i);
            dfs(vc, v, c, res);
            vc.pop_back();
        }
    }
};
