// seem like my old code was bugged?
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
        for (i = 1; i <= rowIndex; ++i) {
            v[f].resize(i + 1, 0);
            v[f][0] = v[nf][0];
            for (j = 1; j < i; ++j) {
                v[f][j] = v[nf][j - 1] + v[nf][j];
            }
            v[f][i] = v[nf][i - 1];
            f = !f;
            nf = !f;
        }
        return v[nf];
    }
};
