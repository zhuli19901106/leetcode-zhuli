class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> v;
        
        dfs(0, 0, v, res, candidates, target);
        return res;
    }
private:
    void dfs(int idx, int sum, vector<int> &v, vector<vector<int>> &res, vector<int> &candidates, int target) {
        if (idx == candidates.size()) {
            if (sum == target) {
                res.push_back(v);
            }
            return;
        }
        int i, j;
        
        for (i = 0; sum + i * candidates[idx] <= target; ++i) {
            for (j = 0; j < i; ++j) {
                v.push_back(candidates[idx]);
            }
            dfs(idx + 1, sum + i * candidates[idx], v, res, candidates, target);
            for (j = 0; j < i; ++j) {
                v.pop_back();
            }
        }
    }
};
