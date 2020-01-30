// https://leetcode.com/problems/maximum-69-number/
#include <string>
using std::stoi;
using std::to_string;

class Solution {
public:
    int maximum69Number (int num) {
        string s = to_string(num);
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            if (s[i] == '6') {
                s[i] = '9';
                break;
            }
        }
        int res = stoi(s);
        return res;
    }
};
