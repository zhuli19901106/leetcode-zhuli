// easy
// https://leetcode.com/problems/defanging-an-ip-address/
#include <string>
using std::string;

class Solution {
public:
    string defangIPaddr(string address) {
        const string &s = address;
        const string fang = "[.]";
        string s1 = "";
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            if (s[i] == '.') {
                s1.append(fang);
            } else {
                s1.push_back(s[i]);
            }
        }
        return s1;
    }
};
