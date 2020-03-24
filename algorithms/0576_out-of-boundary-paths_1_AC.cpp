#include <vector>
using std::vector;

typedef vector<vector<int>> VVI;

class Solution {
public:
    int findPaths(int m, int n, int N, int si, int sj) {
        if (N == 0) {
            return 0;
        }
        
        vector<VVI> g(2);
        int i;
        for (i = 0; i < 2; ++i) {
            g[i].resize(m, vector<int>(n, 0));
        }
        
        int res = 0;
        int f = 0;
        int nf = !f;
        
        g[f][si][sj] = 1;
        res = (res + update(g[f], m, n)) % MOD;
        
        for (i = 1; i < N; ++i) {
            f = !f;
            nf = !f;
            
            nextMove(g[f], g[nf], m, n);
            res = (res + update(g[f], m, n)) % MOD;
        }
        g.clear();
        
        return res;
    }
private:
    static const int MOD = 1000000007;
    
    void nextMove(VVI &gn, VVI &gc, int m, int n) {
        static const int offset[][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};
        
        int i, j;
        int i1, j1;
        int k;
        for (i = 0; i < m; ++i) {
            for (j = 0; j < n; ++j) {
                gn[i][j] = 0;
                for (k = 0; k < 4; ++k) {
                    i1 = i + offset[k][0];
                    j1 = j + offset[k][1];
                    if (i1 < 0 || i1 > m - 1 || j1 < 0 || j1 > n - 1) {
                        continue;
                    }
                    gn[i][j] = (gn[i][j] + gc[i1][j1]) % MOD;
                }
            }
        }
    }
    
    int update(VVI &g, int m, int n) {
        int res = 0;
        int i;
        for (i = 0; i < m; ++i) {
            res = (res + g[i][0]) % MOD;
            res = (res + g[i][n - 1]) % MOD;
        }
        
        int j;
        for (j = 0; j < n; ++j) {
            res = (res + g[0][j]) % MOD;
            res = (res + g[m - 1][j]) % MOD;
        }
        return res;
    }
};
