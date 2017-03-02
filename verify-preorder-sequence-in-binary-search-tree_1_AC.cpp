// The input array can be used as a stack, that's how O(1) space is achieved.
#include <climits>
#include <stack>
#include <vector>
using std::stack;
using std::vector;

class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        auto &a = preorder;
        int n = a.size();
        if (n < 2) {
            return true;
        }
        
        int low = INT_MIN;
        stack<int> st;
        int i;
        for (i = 0; i < n; ++i) {
            if (a[i] < low) {
                return false;
            }
            while (!st.empty() && st.top() < a[i]) {
                low = st.top();
                st.pop();
            }
            st.push(a[i]);
        }
        
        return true;
    }
};
