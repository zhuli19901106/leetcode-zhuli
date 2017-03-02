// Just search it.
#include <vector>
using std::vector;

static const int offset[4][2] = {{-1, -1}, {-1, 0}, {0, -1}, {-1, +1}};

class Solution {
public:
    Solution() {
        b.resize(NR * NC, vector<bool>(NR * NC, true));
        
        b[0][6] = b[6][0] = false;
        b[1][7] = b[7][1] = false;
        b[2][8] = b[8][2] = false;
        
        b[0][2] = b[2][0] = false;
        b[3][5] = b[5][3] = false;
        b[6][8] = b[8][6] = false;
        
        b[0][8] = b[8][0] = false;
        b[2][6] = b[6][2] = false;
    }
    
    int numberOfPatterns(int m, int n) {
        vector<int> a;
        vector<bool> v(NR * NC, false);
        int res = 0;
        dfs(a, v, res, m, n);
        
        return res;
    }
    
    ~Solution() {
        b.clear();
    }
private:
    static const int NR = 3;
    static const int NC = 3;
    vector<vector<bool>> b;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= NR - 1 && y >= 0 && y <= NC - 1;
    }
    
    void dfs(vector<int> &a, vector<bool> &v, int &res, int m, int n) {
        if (a.size() >= m && a.size() <= n) {
            ++res;
        }
        if (a.size() >= n) {
            return;
        }
        
        int i;
        for (i = 0; i < NR * NC; ++i) {
            if (v[i]) {
                continue;
            }
            if (a.size() > 0 && !b[i][a.back()]) {
                continue;
            }
            
            mark(i);
            a.push_back(i);
            v[i] = true;
            
            dfs(a, v, res, m, n);
            
            v[i] = false;
            a.pop_back();
            unmark(i);
        }
    }
    
    void mark(int x) {
        int i = x / NC;
        int j = x % NC;
        int k;
        int i1, j1;
        int i2, j2;
        
        for (k = 0; k < 4; ++k) {
            i1 = i + offset[k][0];
            j1 = j + offset[k][1];
            
            i2 = i - offset[k][0];
            j2 = j - offset[k][1];
            
            if (inbound(i1, j1) && inbound(i2, j2)) {
                b[i1 * NC + j1][i2 * NC + j2] = true;
                b[i2 * NC + j2][i1 * NC + j1] = true;
            }
        }
    }
    
    void unmark(int x) {
        int i = x / NC;
        int j = x % NC;
        int k;
        int i1, j1;
        int i2, j2;
        
        for (k = 0; k < 4; ++k) {
            i1 = i + offset[k][0];
            j1 = j + offset[k][1];
            
            i2 = i - offset[k][0];
            j2 = j - offset[k][1];
            
            if (inbound(i1, j1) && inbound(i2, j2)) {
                b[i1 * NC + j1][i2 * NC + j2] = false;
                b[i2 * NC + j2][i1 * NC + j1] = false;
            }
        }
    }
};
