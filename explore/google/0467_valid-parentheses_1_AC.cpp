#include <stack>
#include <unordered_map>
#include <unordered_set>
using std::stack;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    Solution() {
        lp.insert('(');
        rp[')'] = '(';
        lp.insert('[');
        rp[']'] = '[';
        lp.insert('{');
        rp['}'] = '{';
    }
    
    bool isValid(string s) {
        stack<char> st;
        int n = s.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (lp.find(s[i]) != lp.end()) {
                st.push(s[i]);
            } else if (rp.find(s[i]) != rp.end()) {
                if (!st.empty() && st.top() == rp[s[i]]) {
                    st.pop();
                } else {
                    break;
                }
            } else {
                break;
            }
        }
        return i == n && st.empty();
    }
    
    ~Solution() {
        lp.clear();
        rp.clear();
    }
private:
    unordered_map<char, char> rp;
    unordered_set<char> lp;
};
