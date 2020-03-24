class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size();
        int m = numRows;
        if (m <= 1) {
            // Watch out for boundary cases.
            return s;
        }
        int i, j;
        string res = "";
        
        for (j = 0; j < n; j += 2 * m - 2) {
            res.push_back(s[j]);
        }
        for (i = 1; i < m - 1; ++i) {
            for (j = 0; j < n; j += 2 * m - 2) {
                if (j + i < n) {
                    res.push_back(s[j + i]);
                }
                if (j + 2 * m - 2 - i < n) {
                    res.push_back(s[j + 2 * m - 2 - i]);
                }
            }
        }
        for (j = m - 1; j < n; j += 2 * m - 2) {
            res.push_back(s[j]);
        }
        return res;
    }
};
