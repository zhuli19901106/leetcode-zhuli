#include <stack>
using std::stack;

class MyQueue {
public:
    void push(int x) {
        s1.push(x);
    }

    int pop() {
        int res = peek();
        s2.pop();
        return res;
    }

    int peek() {
        if (!s2.empty()) {
            return s2.top();
        }
        int val;
        while (!s1.empty()) {
            val = s1.top();
            s1.pop();
            s2.push(val);
        }
        return s2.top();
    }

    bool empty() {
        return s1.empty() && s2.empty();
    }
private:
    stack<int> s1, s2;
};
