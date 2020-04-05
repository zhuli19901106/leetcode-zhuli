class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        if (n == 0 || m == 0) {
            return false;
        }
        int x = n - 1;
        int y = 0;
        while (x >= 0 && y <= m - 1) {
            if (matrix[x][y] < target) {
                ++y;
            } else if (matrix[x][y] > target) {
                --x;
            } else {
                return true;
            }
        }
        return false;
    }
};
