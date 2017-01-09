// Power set
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> v;
        
        dfs(0, v, res, nums);
        return res;
    }
private:
    void dfs(int idx, vector<int> &v, vector<vector<int>> &res, 
             vector<int> &nums) {
        if (idx == nums.size()) {
            res.push_back(v);
            return;
        }
        dfs(idx + 1, v, res, nums);
        v.push_back(nums[idx]);
        dfs(idx + 1, v, res, nums);
        v.pop_back();
    }
};