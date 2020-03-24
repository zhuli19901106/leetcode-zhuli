// My version was over 150 lines long and too buggy to be put right, I gave up.
// https://discuss.leetcode.com/topic/34875/easy-short-concise-and-fast-java-dfs-3-ms-solution/2
// This is an exact rewrite of the oroginal java version from @dietpepsi.
#include <algorithm>
#include <string>
#include <vector>
using std::reverse;
using std::string;
using std::vector;

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> res;
        remove(s, 0, 0, res, "()");
        
        return res;
    }
private:
    void remove(const string &s, int last_i, int last_j, vector<string> &res, string p) {
        int ls = s.size();
        int cnt = 0;
        int i, j;
        for (i = last_i; i < ls; ++i) {
            if (s[i] == p[0]) {
                ++cnt;
            } else if (s[i] == p[1]) {
                --cnt;
            }
            if (cnt >= 0) {
                continue;
            }
            for (j = last_j; j <= i; ++j) {
                if (s[j] != p[1]) {
                    continue;
                }
                if (j > last_j && s[j - 1] == p[1]) {
                    continue;
                }
                remove(s.substr(0, j) + s.substr(j + 1, ls - j - 1), i, j, res, p);
            }
            return;
        }
        string s1 = s;
        reverse(s1.begin(), s1.end());
        if (p[0] == '(') {
            remove(s1, 0, 0, res, ")(");
        } else {
            res.push_back(s1);
        }
    }
};
