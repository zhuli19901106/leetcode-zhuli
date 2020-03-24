#include <algorithm>
#include <climits>
using std::min;

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int k = primes.size();
        vector<int> idx(k, 0);
        vector<int> term(k);
        vector<int> res(1, 1);
        int min_val;
        int i, j;
        
        for (i = 1; i < n; ++i) {
            min_val = INT_MAX;
            for (j = 0; j < k; ++j) {
                term[j] = res[idx[j]] * primes[j];
                min_val = min(min_val, term[j]);
            }
            for (j = 0; j < k; ++j) {
                if (min_val == term[j]) {
                    ++idx[j];
                }
            }
            res.push_back(min_val);
        }
        int ret = res[n - 1];
        idx.clear();
        term.clear();
        res.clear();
        
        return ret;
    }
};
