#include <string>
using std::string;

class Solution {
public:
    bool isStrobogrammatic(string num) {
        int ls = num.size();
        static const int d[10] = {0, 1, -1, -1, -1, -1, 9, -1, 8, 6};
        int i = 0;
        int j = ls - 1;
        while (i <= j) {
            if (num[i] - '0' != d[num[j] - '0']) {
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }
};
