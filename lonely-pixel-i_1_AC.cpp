class Solution {
public:
    int findLonelyPixel(vector<vector<char>>& picture) {
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
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (a[i][j] == 'B' && rb[i] == 1 && cb[j] == 1) {
                    ++res;
                }
            }
        }
        rb.clear();
        cb.clear();
        
        return res;
    }
};
