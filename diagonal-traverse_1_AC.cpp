#include <vector>
using std::vector;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        auto &a = matrix;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        vector<int> res;
        
        if (n == 0 || m == 0) {
            return res;
        }
        int i, j;
        bool go_right;
        
        go_right = true;
        i = j = 0;
        while (i + j <= (n - 1) + (m - 1)) {
            res.push_back(a[i][j]);
            if (go_right) {
                if (i > 0 && j < m - 1) {
                    --i;
                    ++j;
                } else if (j < m - 1) {
                    ++j;
                    go_right = !go_right;
                } else {
                    ++i;
                    go_right = !go_right;
                }
            } else {
                if (i < n - 1 && j > 0) {
                    ++i;
                    --j;
                } else if (i < n - 1) {
                    ++i;
                    go_right = !go_right;
                } else {
                    ++j;
                    go_right = !go_right;
                }
            }
        }
        
        return res;
    }
};
