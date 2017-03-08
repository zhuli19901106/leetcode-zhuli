// 2-d binary indexed tree
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        auto &a = matrix;
        n = a.size();
        m = (n > 0 ? a[0].size() : 0);
        c.resize(n + 1, vector<int>(m + 1, 0));
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                add(i + 1, j + 1, a[i][j]);
            }
        }
    }
    
    void update(int row, int col, int val) {
        if (row < 0 || row > n - 1 || col < 0 || col > m - 1) {
            return;
        }
        int old_val = get(row + 1, col + 1);
        add(row + 1, col + 1, val - old_val);
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return sum(row2 + 1, col2 + 1) + sum(row1, col1) - sum(row2 + 1, col1) 
            - sum(row1, col2 + 1);
    }
    
    ~NumMatrix() {
        c.clear();
    }
private:
    int n, m;
    vector<vector<int>> c;
    
    int lowbit(int x ) {
        return x & -x;
    }
    
    void add(int i, int j, int val) {
        if (i < 1 || i > n || j < 1 || j > m) {
            return;
        }
        int x, y;
        for (x = i; x <= n; x += lowbit(x)) {
            for (y = j; y <= m; y += lowbit(y)) {
                c[x][y] += val;
            }
        }
    }
    
    int sum(int i, int j) {
        i = max(i, 0);
        i = min(i, n);
        j = max(j, 0);
        j = min(j, m);
        
        int x, y;
        int s = 0;
        for (x = i; x > 0; x -= lowbit(x)) {
            for (y = j; y > 0; y -= lowbit(y)) {
                s += c[x][y];
            }
        }
        return s;
    }
    
    int get(int i, int j) {
        return sum(i, j) + sum(i - 1, j - 1) - sum(i, j - 1) - sum(i - 1, j);
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */