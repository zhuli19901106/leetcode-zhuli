#include <vector>
using std::vector;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        const int N_DICT = 26;
        vector<int> idx(N_DICT, -(n + 1));
        vector<int> cnt(N_DICT, 0);
        int cc = 0;
        
        int lt = tasks.size();
        int i;
        for (i = 0; i < lt; ++i) {
            ++cnt[tasks[i] - 'A'];
            ++cc;
        }
        
        int m = 0;
        int mc, mi;
        while (cc > 0) {
            mc = mi = -1;
            for (i = 0; i < N_DICT; ++i) {
                if (m - idx[i] <= n || cnt[i] <= 0) {
                    continue;
                }
                if (cnt[i] > mc) {
                    mc = cnt[i];
                    mi = i;
                }
            }
            if (mi != -1) {
                --cnt[mi];
                idx[mi] = m;
                --cc;
            }
            ++m;
        }
        
        return m;
    }
};
