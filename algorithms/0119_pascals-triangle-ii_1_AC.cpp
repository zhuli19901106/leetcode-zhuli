class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex < 0) {
            return vector<int>();
        }
        vector<vector<int>> v(2);
        
        v[0].push_back(1);
        int i, j;
        int f, nf;
        
        f = 1;
        nf = !f;
        for (i = 2; i <= rowIndex + 1; ++i) {
            v[f].resize(i);
            v[f][0] = v[nf][0];
            for (j = 1; j < i; ++j) {
                v[f][j] = v[nf][j - 1] + v[nf][j];
            }
            v[f][i - 1] = v[nf][i - 2];
            f = !f;
            nf = !f;
        }
        return v[nf];
    }
};
