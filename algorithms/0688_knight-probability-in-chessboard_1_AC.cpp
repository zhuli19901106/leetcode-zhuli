#include <vector>
using std::vector;

static int offset[8][2] = {
    {-2, -1}, {-2, +1}, {+2, -1}, {+2, +1}, 
    {-1, -2}, {-1, +2}, {+1, -2}, {+1, +2}
};

class Solution {
public:
    double knightProbability(int N, int K, int r, int c) {
        vector<vector<vector<double>>> dp(2);
        dp[0].resize(N, vector<double>(N, 0));
        dp[1].resize(N, vector<double>(N, 0));
        
        int f, nf;
        nf = 0;
        f = !f;
        dp[nf][r][c] = 1.0;
        
        int ki;
        int i, j;
        int i1, j1;
        int oi;
        for (ki = 0; ki < K; ++ki) {
            for (i = 0; i < N; ++i) {
                for (j = 0; j < N; ++j) {
                    dp[f][i][j] = 0.0;
                }
            }
            for (i = 0; i < N; ++i) {
                for (j = 0; j < N; ++j) {
                    for (oi = 0; oi < 8; ++oi) {
                        i1 = i + offset[oi][0];
                        j1 = j + offset[oi][1];
                        if (i1 < 0 || i1 > N - 1 || j1 < 0 || j1 > N - 1) {
                            // out of bound
                            continue;
                        }
                        dp[f][i1][j1] += dp[nf][i][j] / 8.0;
                    }
                }
            }
            f = !f;
            nf = !f;
        }
        
        double res = 0.0;
        for (i = 0; i < N; ++i) {
            for (j = 0; j < N; ++j) {
                res += dp[nf][i][j];
            }
        }
        
        return res;
    }
};
