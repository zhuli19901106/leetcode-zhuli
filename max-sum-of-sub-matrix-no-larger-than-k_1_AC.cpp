#include <climits>
#include <set>
#include <vector>
using std::set;
using std::vector;

class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        auto &a = matrix;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        if (n == 0 || m == 0) {
            return 0;
        }
        if (n > m) {
            vector<vector<int>> matrix1;
            transpose(matrix, matrix1);
            return maxSumSubmatrix(matrix1, k);
        }
        
        vector<int> s(m);
        int i, j, ii;
        int res = INT_MIN;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                s[j] = 0;
            }
            for (j = i; j < n; ++j) {
                for (ii = 0; ii < m; ++ii) {
                    s[ii] += a[j][ii];
                }
                res = max(res, maxSumSubarray(s, k));
            }
        }
        s.clear();
        
        return res;
    }
private:
    void transpose(vector<vector<int>> &matrix, vector<vector<int>> &matrix1) {
        auto &a = matrix;
        auto &a1 = matrix1;
        int n = a.size();
        int m = n > 0 ? a[0].size() : 0;
        a1.resize(m, vector<int>(n));
        
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                a1[j][i] = a[i][j];
            }
        }
    }
    
    int maxSumSubarray(vector<int> &v, int k) {
        int sum = 0;
        set<int> st;
        int n = v.size();
        int i;
        auto it = st.begin();
        int res = INT_MIN;
        
        st.insert(0);
        for (i = 0; i < n; ++i) {
            sum += v[i];
            it = st.lower_bound(sum - k);
            st.insert(sum);
            if (it == st.end()) {
                // No solution yet.
                continue;
            }
            res = max(res, sum - *it);
            
        }
        st.clear();
        
        return res;
    }
};
