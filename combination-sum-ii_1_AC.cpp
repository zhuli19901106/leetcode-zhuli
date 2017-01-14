#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        int n = candidates.size();
        if (n == 0) {
            return res;
        }
        
        unordered_map<int, int> um;
        vector<int> v, tc, c;
        int i;
        for (i = 0; i < n; ++i) {
            ++um[candidates[i]];
        }
        for (auto it = um.begin(); it != um.end(); ++it) {
            v.push_back(it->first);
            tc.push_back(it->second);
        }
        
        dfs(0, target, c, v, tc, res);
        return res;
    }
private:
    void dfs(int sum, int target, vector<int> &c, vector<int> &v, vector<int> &tc, 
             vector<vector<int>> &res) {
        int idx = c.size();
        if (idx == tc.size()) {
            if (sum == target) {
                int i, j;
                vector<int> a;
                for (i = 0; i < idx; ++i) {
                    for (j = 0; j < c[i]; ++j) {
                        a.push_back(v[i]);
                    }
                }
                res.push_back(a);
            }
            return;
        }
        int i;
        for (i = 0; i <= tc[idx]; ++i) {
            if (sum + i * v[idx] > target) {
                break;
            }
            c.push_back(i);
            dfs(sum + i * v[idx], target, c, v, tc, res);
            c.pop_back();
        }
    }
};
