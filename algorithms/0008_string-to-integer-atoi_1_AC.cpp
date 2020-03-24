// Things like this gets you old.
#include <cctype>
#include <climits>
#include <cstdint>
using std::isdigit;

class Solution {
public:
    int myAtoi(string str) {
        const int R = 10;
        
        int ls = str.size();
        int64_t res = 0;
        int i = 0;
        while (i < ls && str[i] == ' ') {
            ++i;
        }
        if (i >= ls) {
            return res;
        }
        
        int flag = +1;
        if (str[i] == '+') {
            flag = +1;
            ++i;
        } else if (str[i] == '-') {
            flag = -1;
            ++i;
        }
        while (i < ls) {
            if (!isdigit(str[i])) {
                return flag * res;
            }
            res = res * R + (str[i] - '0');
            if (flag * res < INT_MIN) {
                return INT_MIN;
            }
            if (flag * res > INT_MAX) {
                return INT_MAX;
            }
            ++i;
        }
        return flag * res;
    }
};
