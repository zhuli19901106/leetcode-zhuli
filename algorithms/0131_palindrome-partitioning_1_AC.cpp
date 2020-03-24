class Solution {
public:
    vector<vector<string>> partition(string s) {
        int ls = s.size();
        vector<vector<string>> res;
        if (ls == 0) {
            return res;
        }
        
        vector<vector<bool>> is_pal(ls, vector<bool>(ls, false));
        int i, j;
        for (i = 0; i < ls; ++i) {
            is_pal[i][i] = true;
        }
        for (i = 0; i < ls - 1; ++i) {
            is_pal[i][i + 1] = (s[i] == s[i + 1]);
        }
        for (i = 2; i < ls; ++i) {
            for (j = 0; j + i < ls; ++j) {
                is_pal[j][j + i] = (is_pal[j + 1][j + i - 1] && 
                    (s[j] == s[j + i]));
            }
        }
        vector<string> v;
        dfs(0, v, s, res, is_pal);
        return res;
    }
private:
    void dfs(int idx, vector<string> &v, string &s, vector<vector<string>> &res, 
        vector<vector<bool>> &is_pal) {
        int ls = s.size();
        if (idx == ls) {
            res.push_back(v);
            return;
        }
        int i;
        for (i = idx; i < ls; ++i) {
            if (!is_pal[idx][i]) {
                continue;
            }
            v.push_back(s.substr(idx, i - idx + 1));
            dfs(i + 1, v, s, res, is_pal);
            v.pop_back();
        }
    }
};
