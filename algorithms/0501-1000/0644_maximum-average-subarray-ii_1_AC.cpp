// If the answer is not among variables, try to find them among values.
#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        auto &a = nums;
        int n = a.size();
        double ll, mm, rr;
        static const double EPS = 1e-5;
        
        ll = mm = a[0];
        for (auto &x: a) {
            ll = min<double>(ll, x);
            rr = max<double>(rr, x);
        }
        while (rr - ll > EPS) {
            mm = ll + (rr - ll) / 2;
            if (hasLargerAverage(a, k, mm)) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return mm;
    }
private:
    bool hasLargerAverage(vector<int> &a, int k, double ave) {
        int n = a.size();
        double sum, pref_sum, min_sum;
        int i;
        
        sum = pref_sum = min_sum = 0;
        i = 0;
        while (i < k) {
            sum += a[i] - ave;
            ++i;
        }
        if (sum > 0) {
            return true;
        }
        while (i < n) {
            sum += a[i] - ave;
            pref_sum += a[i - k] - ave;
            min_sum = min(min_sum, pref_sum);
            if (sum - min_sum > 0) {
                return true;
            }
            ++i;
        }
        return false;
    }
};
