// F**k this problem
#include <algorithm>
#include <stack>
using std::max;
using std::stack;

class Solution {
public:
    int lengthLongestPath(string s) {
        stack<int> st;
        int ls = s.size();
        
        int sum = 0;
        int res = 0;
        
        bool is_file;
        int tab_cnt;
        
        int i = 0;
        int j;
        while (i < ls) {
            is_file = false;
            tab_cnt = 0;
            j = i;
            while (j < ls && s[j] == '\t') {
                ++j;
                ++tab_cnt;
            }
            
            i = j;
            while (j < ls && s[j] != '\n') {
                if (s[j] == '.') {
                    is_file = true;
                }
                ++j;
            }
            
            while (st.size() > tab_cnt) {
                sum -= st.top();
                st.pop();
            }
            if (is_file) {
                res = max(res, sum + j - i);
            } else {
                st.push(j - i + 1);
                sum += st.top();
            }
            i = j + 1;
        }
        while (!st.empty()) {
            st.pop();
        }
        return res;
    }
};
