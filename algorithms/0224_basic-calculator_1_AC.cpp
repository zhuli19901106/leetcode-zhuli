#include <functional>
#include <unordered_map>
using std::function;
using std::unordered_map;

class Solution {
public:
    Solution() {
        fun["+"] = [](int x, int y) {return x + y;};
        fun["-"] = [](int x, int y) {return x - y;};
        fun["*"] = [](int x, int y) {return x * y;};
        fun["/"] = [](int x, int y) {return x / y;};
        
        pre["("] = -1;
        int p = 0;
        pre["+"] = p;
        pre["-"] = p;
        ++p;
        pre["*"] = p;
        pre["/"] = p;
        ++p;
    }
    
    int calculate(string s) {
        int ls = s.size();
        int res = 0;
        stack<int> nums;
        stack<string> ops;
        
        int i = 0;
        string op;
        while (i < ls) {
            if (s[i] == '+' || s[i] == '-' || s[i] == '*' || 
                s[i] == '/') {
                op.clear();
                op.push_back(s[i++]);
                while (!ops.empty() && pre[ops.top()] >= pre[op]) {
                    calc(nums, ops);
                }
                ops.push(op);
            } else if (s[i] == '(') {
                op.clear();
                op.push_back(s[i++]);
                ops.push(op);
            } else if (s[i] == ')') {
                while (ops.top() != "(") {
                    calc(nums, ops);
                }
                ops.pop();
                ++i;
            } else if (isdigit(s[i])) {
                int val = 0;
                while (i < ls && isdigit(s[i])) {
                    val = val * 10 + (s[i] - '0');
                    ++i;
                }
                nums.push(val);
            } else {
               ++i;
            }
        }
        while (!ops.empty()) {
            calc(nums, ops);
        }
        res = nums.top();
        nums.pop();
        return res;
    }
    
    void calc(stack<int> &nums, stack<string> &ops) {
        if (nums.size() < 2 || ops.size() < 1) {
            return;
        }
        
        string op = ops.top();
        ops.pop();
        int n2 = nums.top();
        nums.pop();
        int n1 = nums.top();
        nums.pop();
        nums.push(fun[op](n1, n2));
    }
    
    ~Solution() {
        fun.clear();
        pre.clear();
    }
private:
    unordered_map<string, function<int(int, int)>> fun;
    unordered_map<string, int> pre;
};
