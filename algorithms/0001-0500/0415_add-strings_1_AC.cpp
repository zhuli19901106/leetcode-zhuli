#include <algorithm>
#include <cstring>
using std::max;
using std::memset;

class Solution {
public:
    string addStrings(string num1, string num2) {
        int len1 = num1.size();
        int len2 = num2.size();
        memset(buf, 0, MAXN * sizeof(int));
        int i;
        for (i = 0; i < len1; ++i) {
            buf[len1 - 1 - i] += num1[i] - '0';
        }
        for (i = 0; i < len2; ++i) {
            buf[len2 - 1 - i] += num2[i] - '0';
        }
        int len = max(len1, len2);
        for (i = 0; i < len; ++i) {
            buf[i + 1] += buf[i] / 10;
            buf[i] %= 10;
        }
        i = len;
        string res = "";
        while (i > 0 && buf[i] == 0) {
            --i;
        }
        while (i >= 0) {
            res.push_back(buf[i] + '0');
            --i;
        }
        return res;
    }
private:
    static const int MAXN = 5105;
    int buf[MAXN];
};
