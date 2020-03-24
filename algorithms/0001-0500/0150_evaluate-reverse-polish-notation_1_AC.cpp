#include <cstdio>
#include <functional>
#include <stack>
#include <unordered_map>
using std::function;
using std::sscanf;
using std::stack;
using std::unordered_map;

class Solution {
public:
    Solution() {
        fun["+"] = [](int x, int y){return x + y;};
        fun["-"] = [](int x, int y){return x - y;};
        fun["*"] = [](int x, int y){return x * y;};
        fun["/"] = [](int x, int y){return x / y;};
    }
    
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int tc = tokens.size();
        int i;
        int n1, n2, n3;
        for (i = 0; i < tc; ++i) {
            if (fun.find(tokens[i]) == fun.end()) {
                sscanf(tokens[i].data(), "%d", &n1);
                st.push(n1);
            } else {
                n2 = st.top();
                st.pop();
                n1 = st.top();
                st.pop();
                n3 = fun[tokens[i]](n1, n2);
                st.push(n3);
            }
        }
        
        n3 = st.top();
        st.pop();
        return n3;
    }
    
    ~Solution() {
        fun.clear();
    }
private:
    unordered_map<string, function<int(int, int)>> fun;
};
