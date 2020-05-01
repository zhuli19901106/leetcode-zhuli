#include <cctype>
#include <stack>
using std::isalpha;
using std::isdigit;

class Solution {
public:
    string decodeString(string s) {
        int idx = 0;
        int ls = s.size();
        return parse(s, idx, ls);
    }
private:
    string parse(string &s, int &idx, const int &ls) {
        string res = "";
        int cnt;
        while (idx < ls) {
            if (s[idx] == ']') {
                ++idx;
                return res;
            }
            if (isalpha(s[idx])) {
                res.push_back(s[idx++]);
            } else if (isdigit(s[idx])) {
                cnt = 0;
                while (idx < ls && isdigit(s[idx])) {
                    cnt = cnt * 10 + (s[idx++] - '0');
                }
                ++idx;
                string partial_res = parse(s, idx, ls);
                int i;
                for (i = 0; i < cnt; ++i) {
                    res += partial_res;
                }
            } else {
                ++idx;
            }
        }
        return res;
    }
};
