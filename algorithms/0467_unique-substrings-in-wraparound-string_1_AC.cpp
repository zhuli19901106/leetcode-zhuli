// Use bit manipulation to save some space.
#include <algorithm>
#include <map>
using std::map;
using std::min;

class Solution {
public:
    int findSubstringInWraproundString(string p) {
        static const int R = 26;
        int lp = p.size();
        int i, j, k, ii;
        int len, len1;
        map<int, int> mm;
        int idx;
        
        i = 0;
        while (i < lp) {
            j = i + 1;
            while (j < lp && p[j] == (p[j - 1] - 'a' + 1) % R + 'a') {
                ++j;
            }
            len = j - i;
            for (k = len; k >= 1; --k) {
                if (mm[k] == (1 << R) - 1) {
                    // Already full
                    break;
                }
                len1 = min(len - k + 1, R);
                for (ii = 0; ii < len1; ++ii) {
                    idx = p[i + ii] - 'a';
                    mm[k] |= (1 << idx);
                }
            }
            i = j;
        }
        
        int val;
        int res = 0;
        for (auto it = mm.rbegin(); it != mm.rend(); ++it) {
            k = it->first;
            val = it->second;
            if (val == (1 << R) - 1) {
                res += k * R;
                break;
            } else {
                res += countOnes(val);
            }
        }
        mm.clear();
        
        return res;
    }
private:
    int countOnes(int x) {
        int cnt = 0;
        while (x != 0) {
            x = (x & x - 1);
            ++cnt;
        }
        return cnt;
    }
};
