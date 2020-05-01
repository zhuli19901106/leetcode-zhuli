// You can't come up with a good solution for a bad problem.
// There is no pure O(1) solution if you use queues to implement stacks.
#include <queue>
using std::queue;

class MyStack {
public:
    MyStack() {
        f = 0;
        nf = !f;
    }

    void push(int x) {
        q[nf].push(x);
    }

    int pop() {
        int res;
        while (q[nf].size() > 1) {
            q[f].push(q[nf].front());
            q[nf].pop();
        }
        if (q[nf].size() == 1) {
            res = q[nf].front();
            q[nf].pop();
            return res;
        }

        while (q[f].size() > 1) {
            q[nf].push(q[f].front());
            q[f].pop();
        }
        f = nf;
        nf = !f;

        res = q[nf].front();
        q[nf].pop();
        return res;
    }

    int top() {
        while (q[nf].size() > 1) {
            q[f].push(q[nf].front());
            q[nf].pop();
        }
        if (q[nf].size() == 1) {
            return q[nf].front();
        }

        while (q[f].size() > 1) {
            q[nf].push(q[f].front());
            q[f].pop();
        }
        f = nf;
        nf = !f;

        return q[nf].front();
    }

    bool empty() {
        return q[f].size() + q[nf].size() == 0;
    }
private:
    queue<int> q[2];
    int f, nf;
};