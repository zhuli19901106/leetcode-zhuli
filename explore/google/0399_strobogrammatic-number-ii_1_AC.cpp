#include <string>
#include <vector>
using std::string;
using std::vector;

static const int d[10] = {0, 1, -1, -1, -1, -1, 9, -1, 8, 6};

class Solution {
public:
    Solution() {
        int i;
        for (i = 0; i < 10; ++i) {
            if (d[i] != -1) {
                v1.push_back(i);
            }
            if (d[i] == i) {
                v2.push_back(i);
            }
        }
    }
    
    vector<string> findStrobogrammatic(int n) {
        vector<string> res;
        if (n <= 0) {
            return res;
        }
        
        string s;
        dfs(s, n, res);
        
        return res;
    }
private:
    vector<int> v1, v2;
    
    void dfs(string &s, int n, vector<string> &res) {
        int ls = s.size();
        int i;
        
        if (ls == n / 2) {
            string s1 = "";
            for (i = ls - 1; i >= 0; --i) {
                s1.push_back(d[s[i] - '0'] + '0');
            }
            string ss;
            if (n % 2 == 0) {
                ss = s + s1;
                res.push_back(ss);
            } else {
                ss = s + '0' + s1;
                for (auto &val: v2) {
                    ss[ls] = val + '0';
                    res.push_back(ss);
                }
            }
            return;
        }
        
        for (auto &val: v1) {
            if (ls == 0 && val == 0) {
                continue;
            }
            s.push_back(val + '0');
            dfs(s, n, res);
            s.pop_back();
        }
    }
};
