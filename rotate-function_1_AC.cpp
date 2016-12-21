#include <algorithm>
#include <cstdint>
using std::max;

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int n = A.size();
        if (n == 0) {
            return 0;
        }
        int64_t f = 0;
        int64_t sum = 0;
        int i;
        for (i = 0; i < n; ++i) {
            f += i * A[i];
            sum += A[i];
        }
        int64_t maxVal = f;
        for (i = n - 1; i > 0; --i) {
            f += sum - 1LL * n * A[i];
            maxVal = max(maxVal, f);
        }
        return maxVal;
    }
};
