class Solution {
public:
    Solution() {
        local.resize(2);
        local[1].push_back("()");
        global = local;
    }
    
    vector<string> generateParenthesis(int n) {
        while (global.size() <= n) {
            generateNextResult();
        }
        return global[n];
    }
private:
    vector<vector<string>> local;
    vector<vector<string>> global;
    
    void generateNextResult() {
        int n = global.size();
        int i, j, k;
        int n1, n2;
        
        local.push_back(vector<string>());
        global.push_back(vector<string>());
        
        n1 = global[n - 1].size();
        for (i = 0; i < n1; ++i) {
            local[n].push_back("(" + global[n - 1][i] + ")");
        }
        n1 = local[n].size();
        for (i = 0; i < n1; ++i) {
            global[n].push_back(local[n][i]);
        }
        
        for (k = 1; k <= n - 1; ++k) {
            n1 = local[k].size();
            n2 = global[n - k].size();
            for (i = 0; i < n1; ++i) {
                for (j = 0; j < n2; ++j) {
                    global[n].push_back(local[k][i] + global[n - k][j]);
                }
            }
        }
    }
};
