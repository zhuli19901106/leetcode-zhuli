class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) { 
        vector<vector<int>> res;
        this->k = k;
        this->n = n;
        combination(1, 0, res);
        return res;
    }
private:
    static const int N_MAX = 9;
    int n;
    int k;
    vector<int> v;
    
    void combination(int idx, int sum, vector<vector<int>> &res) {
        if (v.size() == k) {
            if (sum == n) {
                res.push_back(v);
            }
            return;
        }
        int i;
        for (i = idx; i <= (n - sum) / (k - v.size()); ++i) {
            if (i > N_MAX) {
                break;
            }
            v.push_back(i);
            combination(i + 1, sum + i, res);
            v.pop_back();
        }
    }
};
