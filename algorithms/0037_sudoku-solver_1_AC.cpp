// Brute-force backtracking
#include <cmath>
#include <vector>
using std::sqrt;
using std::vector;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        auto &a = board;
        n = a.size();
        if (n == 0) {
            return;
        }
        nr = (int)sqrt(n);
        ns = n * n;
        
        row.resize(n, 0);
        col.resize(n, 0);
        block.resize(n, 0);
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                if (a[i][j] == '.') {
                    pos.push_back(i * n + j);
                } else {
                    mark(i, j, a[i][j] - '0');
                }
            }
        }
        
        bool suc = dfs(a);
        
        row.clear();
        col.clear();
        block.clear();
        pos.clear();
        n = nr = ns = 0;
    }
private:
    int n, nr, ns;
    vector<int> row, col, block;
    vector<int> pos;
    
    void mark(int x, int y, int d) {
        int bt = (1 << d - 1);
        row[x] ^= bt;
        col[y] ^= bt;
        block[x / nr * nr + y / nr] ^= bt;
    }
    
    bool dfs(vector<vector<char>> &a) {
        if (pos.size() == 0) {
            // Done
            return true;
        }
        
        int idx = pos.back();
        int x = idx / n;
        int y = idx % n;
        int d;
        int bt;
        for (d = 1; d <= n; ++d) {
            bt = (1 << d - 1);
            if (row[x] & bt) {
                continue;
            }
            if (col[y] & bt) {
                continue;
            }
            if (block[x / nr * nr + y / nr] & bt) {
                continue;
            }
            
            pos.pop_back();
            mark(x, y, d);
            a[x][y] = d + '0';
            if (dfs(a)) {
                return true;
            }
            a[x][y] = '.';
            mark(x, y, d);
            pos.push_back(idx);
        }
        return false;
    }
};
