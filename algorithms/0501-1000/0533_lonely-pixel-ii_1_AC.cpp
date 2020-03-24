class Solution {
public:
    int findBlackPixel(vector<vector<char>>& picture, int N) {
        auto &a = picture;
        int n = a.size();
        int m = (n > 0 ? a[0].size() : 0);
        
        if (n == 0 || m == 0) {
            return 0;
        }
        
        vector<int> rb(n, 0), cb(m, 0);
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == 'B') {
                    ++rb[i];
                    ++cb[j];
                }
            }
        }
        
        vector<string> vh;
        string h;
        int val;
        int k;
        for (i = 0; i < n; ++i) {
            h = "";
            for (j = 0; j < m; j += 8) {
                val = 0;
                for (k = 0; k < 8; ++k) {
                    val = (val << 1) + (j + k < m && a[i][j + k] == 'B' ? 1 : 0);
                }
                h.push_back(val);
            }
            vh.push_back(h);
        }
        
        int res = 0;
        int cnt;
        for (j = 0; j < m; ++j) {
            if (cb[j] != N) {
                continue;
            }
            for (i = 0; i < n; ++i) {
                if (a[i][j] == 'W' || rb[i] != N) {
                    continue;
                }
                h = vh[i];
            }
            
            cnt = 0;
            for (i = 0; i < n; ++i) {
                if (a[i][j] == 'W' || rb[i] != N) {
                    continue;
                }
                if (h != vh[i]) {
                    break;
                }
                ++cnt;
            }
            if (cnt == N) {
                res += N;
            }
        }
        
        vh.clear();
        rb.clear();
        cb.clear();
        
        return res;
    }
};
