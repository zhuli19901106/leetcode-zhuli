#include <stack>
using std::stack;

class Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
        s1.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        peek();
        s2.pop();
    }

    // Get the front element.
    int peek(void) {
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

    // Return whether the queue is empty.
    bool empty(void) {
        return s1.empty() && s2.empty();
    }
private:
    stack<int> s1, s2;
};
