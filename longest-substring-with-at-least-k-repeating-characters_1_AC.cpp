// The code was ugly, but it passed with one shot.
// I'm a bit surprised, actually.
// I can figure out other solutions, but D&C is more intuitive, thus easy to understand.
// Just forget about it.
#include <algorithm>
#include <cstring>
using std::memset;

class Solution {
public:
    int longestSubstring(string s, int k) {
        int ls = s.size();
        return solve(s, 0, ls - 1, k);
    }
private:
    static const int DICT_SIZE = 26;
    
    int solve(string &s, int left, int right, int repeat) {
        int res = 0;
        int cnt[DICT_SIZE];
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        int i, j;
        for (i = left; i <= right; ++i) {
            ++cnt[s[i] - 'a'];
        }
        
        int useless = 0;
        for (i = 0; i < DICT_SIZE; ++i) {
            if (cnt[i] > 0 && cnt[i] < repeat) {
                cnt[i] = -1;
                ++useless;
            }
        }
        if (useless == 0) {
            return right - left + 1;
        }
        
        i = left;
        while (true) {
            while (i <= right && cnt[s[i] - 'a'] < repeat) {
                ++i;
            }
            if (i > right) {
                break;
            }
            j = i + 1;
            while (j <= right && cnt[s[j] - 'a'] >= repeat) {
                ++j;
            }
            res = max(res, solve(s, i, j - 1, repeat));
            i = j;
        }
        return res;
    }
};
