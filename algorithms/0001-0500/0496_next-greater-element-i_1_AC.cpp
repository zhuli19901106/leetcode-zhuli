#include <stack>
#include <unordered_map>
using std::stack;
using std::unordered_map;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        stack<int> st;
        unordered_map<int, int> um;
        vector<int> res;
        
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            while (!st.empty() && nums[i] > st.top()) {
                um[st.top()] = nums[i];
                st.pop();
            }
            st.push(nums[i]);
        }
        
        n = findNums.size();
        res.resize(n, -1);
        for (i = 0; i < n; ++i) {
            if (um.find(findNums[i]) != um.end()) {
                res[i] = um[findNums[i]];
            }
        }
        
        while (!st.empty()) {
            st.pop();
        }
        um.clear();
        
        return res;
    }
};
