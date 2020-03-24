class Solution {
public:
    Solution() {
        res.push_back(vector<int>());
        res[0].push_back(0);
    }
    
    vector<int> grayCode(int n) {
        while (res.size() <= n) {
            generateNextGroup();
        }
        return res[n];
    }
private:
    vector<vector<int>> res;
    
    void generateNextGroup() {
        int n = res.size();
        res.push_back(vector<int>());
        int mask = 1 << n - 1;
        int len = res[n - 1].size();
        int i;
        for (i = 0; i <= len - 1; ++i) {
            res[n].push_back(res[n - 1][i]);
        }
        for (i = len - 1; i >= 0; --i) {
            res[n].push_back(res[n - 1][i] | mask);
        }
    }
};
