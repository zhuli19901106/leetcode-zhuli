// Brute-force DFS
// There can't be so many of those "beautiful arrangements".
// So just do it.
class Solution {
public:
    int countArrangement(int N) {
        this->N = N;
        this->m.resize(N + 1, vector<bool>(N + 1, false));
        int i, j;
        for (i = 1; i <= N; ++i) {
            for (j = 1; j <= N; ++j) {
                if (i % j == 0 || j % i == 0) {
                    m[i][j] = true;
                }
            }
        }
        
        vector<int> v;
        vector<bool> b(N + 1, false);
        int res = 0;
        dfs(v, b, res);
        
        m.clear();
        b.clear();
        
        return res;
    }
private:
    int N;
    vector<vector<bool>> m;
    
    void dfs(vector<int> &v, vector<bool> &b, int &res) {
        if (v.size() == N) {
            ++res;
            return;
        }
        int i;
        int j = v.size() + 1;
        for (i = 1; i <= N; ++i) {
            if (b[i] || !m[i][j]) {
                continue;
            }
            v.push_back(i);
            b[i] = true;
            dfs(v, b, res);
            b[i] = false;
            v.pop_back();
        }
    }
};
