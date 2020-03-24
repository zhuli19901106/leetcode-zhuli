// If you don't one-shot, you're dead.
#include <vector>
using std::vector;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        auto &a = flowerbed;
        int na = a.size();
        int i, j;
        int cnt;
        int len;
        
        cnt = 0;
        i = 0;
        while (i < na) {
            if (a[i] == 1) {
                ++i;
                continue;
            }
            j = i + 1;
            while (j < na && a[j] == 0) {
                ++j;
            }
            len = j - i;
            if (i == 0) {
                ++len;
            }
            if (j == na) {
                ++len;
            }
            cnt += (len - 1) / 2;
            i = j;
        }
        return cnt >= n;
    }
};
