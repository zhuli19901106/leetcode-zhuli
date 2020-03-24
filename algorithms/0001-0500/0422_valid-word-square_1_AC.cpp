// Brute-force and straight-forward
#include <algorithm>
#include <string>
#include <vector>
using std::max;
using std::string;
using std::vector;

class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        auto &a = words;
        int n = a.size();
        int m = 0;
        int i;
        for (i = 0; i < n; ++i) {
            m = max(m, (int)a[i].size());
        }
        
        
        int j;
        int len;
        char c1, c2;
        int nm = max(n, m);
        for (i = 0; i < nm; ++i) {
            for (j = i; j < nm; ++j) {
                c1 = get(a, i, j);
                c2 = get(a, j, i);
                if (c1 != c2) {
                    return false;
                }
            }
        }
        return true;
    }
private:
    char get(vector<string> &a, int i, int j) {
        return (a.size() > i && a[i].size() > j) ? a[i][j] : '\0';
    }
};
