class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = n > 0 ? matrix[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        int ll = 0;
        int rr = n * m - 1;
        int mm;
        while (ll <= rr) {
            mm = ll + (rr - ll >> 1);
            if (target < matrix[mm / m][mm % m]) {
                rr = mm - 1;
            } else if (target > matrix[mm / m][mm % m]) {
                ll = mm + 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
