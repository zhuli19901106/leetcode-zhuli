// Understand the mechanism of KMP algorithm.
#include <vector>
using std::vector;

class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        vector<int> next;
        calcNext(str, next);
        int n = str.size();
        int m = n - next[n];
        next.clear();
        return n > m && n % m == 0;
    }
private:
    void calcNext(string& str, vector<int>& next) {
        int i = 0;
        int j = -1;
        int n = str.size();
        next.resize(n + 1);
        next[0] = -1;
        while (i < n) {
            if (j == -1 || str[i] == str[j]) {
                next[++i] = ++j;
            } else {
                j = next[j];
            }
        }
    }
};
