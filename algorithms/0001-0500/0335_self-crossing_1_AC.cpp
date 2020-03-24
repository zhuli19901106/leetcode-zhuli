// https://discuss.leetcode.com/topic/38084/re-post-2-o-n-c-0ms-solutions/5
// A billiant solution from @cartierzhou
#include <vector>
using std::vector;

class Solution {
public:
    bool isSelfCrossing(vector<int> &x) {
        int n = x.size();
        if (n <= 3) {
            return false;
        }
        
        bool grow = (x[2] > x[0]);
        int i;
        for (i = 3; i < n; ++i) {
            if (!grow && x[i] >= x[i - 2]) {
                return true;
            }
            if (grow && x[i] <= x[i - 2]) {
                grow = false;
                if (x[i] == x[i - 2] || (i > 3 && (x[i] >= x[i - 2] - x[i - 4]))) {
                    x[i - 1] -= x[i - 3];
                }
            }
        }
        
        return false;
    }
};
