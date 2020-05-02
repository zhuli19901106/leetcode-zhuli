/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
#include <stack>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::stack;
using std::vector;

class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        auto &nl =nestedList;
        stack<pair<int, const vector<NestedInteger> *>> st;
        stack<int> si;
        int sum = 0;
        
        st.push(make_pair(1, &nl));
        si.push(0);
        
        int i;
        int d;
        const vector<NestedInteger> *pv;
        while (!st.empty()) {
            d = st.top().first;
            pv = st.top().second;
            i = si.top();
            
            if (i == pv->size()) {
                st.pop();
                si.pop();
            } else if ((*pv)[i].isInteger()) {
                sum += (*pv)[i].getInteger() * d;
                ++si.top();
            } else {
                ++si.top();
                st.push(make_pair(d + 1, &((*pv)[i].getList())));
                si.push(0);
            }
        }
        return sum;
    }
};
