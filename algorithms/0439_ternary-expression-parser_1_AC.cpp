#include <cctype>
#include <stack>
#include <string>
#include <vector>
using std::isdigit;
using std::stack;
using std::string;
using std::vector;

class Solution {
public:
    string parseTernary(string expression) {
        auto &s = expression;
        vector<string> tk;
        tokenize(s, tk);
        
        stack<string> sc;
        stack<int> si;
        stack<string> sv;
        
        int n = tk.size();
        int i;
        for (i = 0; i < n; i += 2) {
            if (i + 1 < n && tk[i + 1] == "?") {
                sc.push(tk[i]);
                si.push(0);
            } else {
                sv.push(tk[i]);
                ++si.top();
            }
            while (!si.empty() && si.top() == 2) {
                parse(sc, si, sv);
            }
        }
        while (!si.empty() && si.top() == 2) {
            parse(sc, si, sv);
        }
        string res = sv.top();
        sv.pop();
        
        return res;
    }
private:
    void tokenize(const string &s, vector<string> &v) {
        int ls = s.size();
        int i, j;
        string t;
        
        i = 0;
        while (i < ls) {
            if (!isdigit(s[i])) {
                t.push_back(s[i++]);
                v.push_back(t);
                t.clear();
                continue;
            }
            j = i;
            while (j < ls && isdigit(s[j])) {
                t.push_back(s[j++]);
            }
            v.push_back(t);
            t.clear();
            i = j;
        }
    }
    
    void parse(stack<string> &sc, stack<int> &si, stack<string> &sv) {
        string c = sc.top();
        sc.pop();
        string s2 = sv.top();
        sv.pop();
        string s1 = sv.top();
        sv.pop();
        
        si.pop();
        if (c == "T") {
            sv.push(s1);
        } else {
            sv.push(s2);
        }
        if (!si.empty()) {
            ++si.top();
        }
    }
};
