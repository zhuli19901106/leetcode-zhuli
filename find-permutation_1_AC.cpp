// Solution from @StefanPochmann
// https://discuss.leetcode.com/topic/76276/1-liner-and-5-liner-visual-explanation
// The idea is brilliant.
// Maybe I'm just meant to be stupid.
#include <algorithm>
#include <string>
#include <vector>
using std::reverse;
using std::string;
using std::vector;

class Solution {
public:
    vector<int> findPermutation(string s) {
        int ls = s.size();
        vector<int> v(ls + 1);
        
        int i;
        for (i = 0; i <= ls; ++i) {
            v[i] = i + 1;
        }
        
        int j;
        i = 0;
        while (i < ls) {
            if (s[i] == 'I') {
                ++i;
                continue;
            }
            j = i + 1;
            while (j < ls && s[j] == 'D') {
                ++j;
            }
            reverse(v.begin() + i, v.begin() + j + 1);
            i = j;
        }
        return v;
    }
};
