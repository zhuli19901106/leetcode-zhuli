#include <cstdio>
#include <stack>
#include <string>
#include <vector>
using std::sscanf;
using std::stack;
using std::string;
using std::vector;

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        stack<int> si, st;
        int i, t;
        
        vector<string> vs;
        int len;
        for (string &log: logs) {
            split(log, vs, ':');
            sscanf(vs[0].data(), "%d", &i);
            sscanf(vs[2].data(), "%d", &t);
            if (vs[1] == "start") {
                si.push(i);
                st.push(t);
            } else if (vs[1] == "end") {
                t += 1;
                if (si.top() != i) {
                    // not supposed to happen
                    return vector<int>();
                }
                len = t - st.top();
                res[i] += len;
                si.pop();
                st.pop();
                if (!si.empty()) {
                    res[si.top()] -= len;
                }
            }
        }
        
        return res;
    }
private:
    void split(const string &s, vector<string> &vs, char del) {
        int ls = s.size();
        int i;
        string ss;
        
        vs.clear();
        i = 0;
        while (true) {
            if (i < ls && s[i] != del) {
                ss.push_back(s[i]);
            } else if (ss.size() > 0) {
                vs.push_back(ss);
                ss.clear();
            }
            if (i < ls) {
                ++i;
            } else {
                break;
            }
        }
    }
};
