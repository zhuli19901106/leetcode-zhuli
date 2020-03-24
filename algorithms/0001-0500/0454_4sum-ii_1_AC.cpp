#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> uab, ucd;
        int na = A.size();
        int nb = B.size();
        int nc = C.size();
        int nd = D.size();
        int i, j;
        
        for (i = 0; i < na; ++i) {
            for (j = 0; j < nb; ++j) {
                ++uab[A[i] + B[j]];
            }
        }
        for (i = 0; i < nc; ++i) {
            for (j = 0; j < nd; ++j) {
                ++ucd[C[i] + D[j]];
            }
        }
        
        unordered_map<int, int>::const_iterator it1, it2;
        int res = 0;
        for (it1 = uab.begin(); it1 != uab.end(); ++it1) {
            it2 = ucd.find(-(it1->first));
            if (it2 != ucd.end()) {
                res += it1->second * it2->second;
            }
        }
        uab.clear();
        ucd.clear();
        
        return res;
    }
};
