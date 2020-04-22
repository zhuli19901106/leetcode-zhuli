// Use binary search.
// Special treatment for edge cases.
#include <algorithm>
#include <string>
#include <vector>
using std::max;
using std::string;
using std::upper_bound;
using std::vector;

class Solution {
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        int nr = rows;
        int nc = cols;
        
        vector<int> v;
        int max_len = 0;
        int sum = 0;
        int i;
        
        v.push_back(sum);
        int n = sentence.size();
        for (i = 0; i < n; ++i) {
            max_len = max(max_len, (int)sentence[i].size());
            sum += sentence[i].size();
            v.push_back(sum);
            ++sum;
            v.push_back(sum);
        }
        if (max_len > nc) {
            v.clear();
            return 0;
        }
        
        int j, k;
        int len;
        int res = 0;
        i = 0;
        j = 1;
        len = nc;
        while (i < nr) {
            if (j == 1 && len / v.back() > 0) {
                res += len / v.back();
                len %= v.back();
                continue;
            }
            
            k = upper_bound(v.begin(), v.end(), len + v[j - 1]) - v.begin();
            k |= 1;
            if (k <= j) {
                ++i;
                len = nc;
                continue;
            }
            len -= v[k - 1] - v[j - 1];
            if (k == v.size()) {
                j = 1;
                ++res;
            } else {
                j = k;
            }
        }
        v.clear();
        return res;
    }
};
