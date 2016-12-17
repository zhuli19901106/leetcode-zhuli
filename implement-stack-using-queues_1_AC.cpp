// You can't come up with a good solution for a bad problem.
// There is no pure O(1) solution if you use queues to implement stacks.
// I don't wanna waste time on this problem, so I copied my old code.
#include <queue>
using std::queue;

class Stack {
public:
	Stack() {
		f = 0;
		nf = !f;
	}
	
    // Push element x onto stack.
    void push(int x) {
		q[nf].push(x);
    }

    // Removes the element on top of the stack.
    void pop() {
		while (q[nf].size() > 1) {
			q[f].push(q[nf].front());
			q[nf].pop();
		}
		if (q[nf].size() == 1) {
			q[nf].pop();
			return;
		}
		
		while (q[f].size() > 1) {
			q[nf].push(q[f].front());
			q[f].pop();
		}
		f = nf;
		nf = !f;
		
		q[nf].pop();
    }

    // Get the top element.
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

    // Return whether the stack is empty.
    bool empty() {
		return q[f].size() + q[nf].size() == 0;
    }
private:
	queue<int> q[2];
	int f, nf;
};