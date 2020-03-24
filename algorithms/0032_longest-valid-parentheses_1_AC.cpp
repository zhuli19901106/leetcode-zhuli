// A smart way of using stack.
#include <algorithm>
#include <unordered_map>
using std::max;
using std::unordered_map;

class Solution {
public:
    int longestValidParentheses(string s) {
        int ls = s.size();
        int res = 0;
        int cnt;
        unordered_map<int, int> um;
        
        int i;
        cnt = 0;
        um[0] = -1;
        for (i = 0; i < ls; ++i) {
            if (s[i] == '(') {
                ++cnt;
                if (um.find(cnt) == um.end()) {
                    um[cnt] = i;
                }
            } else if (s[i] == ')') {
                if (um.find(cnt) != um.end()) {
                    um.erase(cnt);
                }
                --cnt;
                if (um.find(cnt) == um.end()) {
                    um[cnt] = i;
                } else {
                    res = max(res, i - um[cnt]);
                }
            }
        }
        um.clear();
        
        return res;
    }
};
