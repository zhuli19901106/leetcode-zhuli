#include <stack>
#include <vector>
using std::stack;
using std::vector;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        if (n == 0) {
            return res;
        }
        res.resize(n, -1);
        
        stack<int> st;
        int i;
        for (i = 0; i < 2 * n; ++i) {
            while (!st.empty() && nums[i % n] > nums[st.top()]) {
                res[st.top()] = nums[i % n];
                st.pop();
            }
            if (i < n) {
                st.push(i);
            }
        }
        
        while (!st.empty()) {
            st.pop();
        }
        
        return res;
    }
};
