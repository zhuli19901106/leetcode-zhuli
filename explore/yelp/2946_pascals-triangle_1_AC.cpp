class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> v;
        if (numRows <= 0) {
            return v;
        }
        v.resize(numRows);
        v[0].push_back(1);
        int i, j;
        for (i = 1; i < numRows; ++i) {
            v[i].push_back(v[i - 1][0]);
            for (j = 1; j < i; ++j) {
                v[i].push_back(v[i - 1][j - 1] + v[i - 1][j]);
            }
            v[i].push_back(v[i - 1][i - 1]);
        }
        return v;
    }
};
