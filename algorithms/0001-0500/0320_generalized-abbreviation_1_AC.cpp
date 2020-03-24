#include <string>
#include <vector>
using std::string;
using std::to_string;
using std::vector;

class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        if (word.size() == 0) {
            res.push_back(word);
            return res;
        }
        
        string s;
        dfs(0, 1, s, res, word);
        dfs(0, 2, s, res, word);
        
        return res;
    }
private:
    void dfs(int idx, int type, string &s, vector<string> &res, const string &w) {
        int lw = w.size();
        if (idx == lw) {
            res.push_back(s);
            return;
        }
        
        int c;
        int i;
        if (type == 1) {
            // Letters
            for (c = 1; c + idx <= lw; ++c) {
                for (i = 0; i < c; ++i) {
                    s.push_back(w[idx + i]);
                }
                dfs(idx + c, 3 - type, s, res, w);
                for (i = 0; i < c; ++i) {
                    s.pop_back();
                }
            }
        } else if (type == 2) {
            // Digits
            string d;
            int ld;
            for (c = 1; c + idx <= lw; ++c) {
                d = to_string(c);
                ld = d.size();
                for (i = 0; i < ld; ++i) {
                    s.push_back(d[i]);
                }
                dfs(idx + c, 3 - type, s, res, w);
                for (i = 0; i < ld; ++i) {
                    s.pop_back();
                }
            }
        }
    }
};
