// Standard DFS
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> v;
        vector<vector<int>> res;
        
        dfs(1, v, res, n, k);
        return res;
    }
private:
    void dfs(int idx, vector<int> &v, vector<vector<int>> &res, int n, int k) {
        if (v.size() == k) {
            res.push_back(v);
            return;
        }
        int i;
        for (i = idx; i <= n + 1 - k + v.size(); ++i) {
            v.push_back(i);
            dfs(i + 1, v, res, n, k);
            v.pop_back();
        }
    }
};
