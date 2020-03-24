#include <algorithm>
#include <cstring>
using std::max;
using std::memset;

class Solution {
public:
    int characterReplacement(string s, int k) {
        const int DICT_SIZE = 26;
        int cnt[DICT_SIZE];
        int i, j;
        int ls = s.size();
        int mi;
        int res = 0;
        
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        i = 0;
        for (j = 0; j < ls; ++j) {
            ++cnt[s[j] - 'A'];
            while (true) {
                // Keep shifting forward until satisfied
                mi = getMaxIndex(cnt, DICT_SIZE);
                if (j - i + 1 - cnt[mi] > k) {
                    --cnt[s[i++] - 'A'];
                } else {
                    break;
                }
            }
            res = max(res, j - i + 1);
        }
        return res;
    }
private:
    int getMaxIndex(int a[], int n) {
        if (a == NULL) {
            return -1;
        }
        int mi = 0;
        int i;
        for (i = 1; i < n; ++i) {
            if (a[i] > a[mi]) {
                mi = i;
            }
        }
        return mi;
    }
};
