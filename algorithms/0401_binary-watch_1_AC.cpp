// The code could be cleaner.
#include <cstdio>
using std::sprintf;

class Solution {
public:
    Solution() {
        int i;
        table.resize(6);
        for (i = 0; i < 60; ++i) {
            table[countOnes(i)].push_back(i);
        }
    }
    
    vector<string> readBinaryWatch(int num) {
        int i, j, k;
        int n1, n2;
        char buf[10];
        vector<string> res;
        for (i = 0; i <= num; ++i) {
            if (i > 4 || num - i > 5) {
                // At most 4 '1's for 24 and 5 '1's for 60.
                continue;
            }
            n1 = table[i].size();
            n2 = table[num - i].size();
            for (j = 0; j < n1; ++j) {
                if (table[i][j] >= 12) {
                    continue;
                }
                for (k = 0; k < n2; ++k) {
                    sprintf(buf, "%d:%02d", table[i][j], table[num - i][k]);
                    res.push_back(string(buf));
                }
            }
        }
        return res;
    }
    
    ~Solution() {
        table.clear();
    }
private:
    vector<vector<int>> table;
    
    int countOnes(int x) {
        int cnt = 0;
        while (x != 0) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    }
};
