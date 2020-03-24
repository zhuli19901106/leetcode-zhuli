/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
#include <algorithm>
#include <stack>
#include <utility>
#include <vector>
using std::make_pair;
using std::max;
using std::pair;
using std::stack;
using std::vector;

class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int res = 0;
        int sum = 0;
        int max_depth = 0;
        stack<pair<int, vector<NestedInteger> *>> st;
        stack<int> si;
        
        st.push(make_pair(1, &nestedList));
        si.push(0);
        max_depth = max(max_depth, (int)st.size());
        
        vector<NestedInteger> *pv;
        int idx;
        int val;
        int level;
        while (!st.empty()) {
            pv = st.top().second;
            idx = si.top();
            ++si.top();
            if (idx == pv->size()) {
               st.pop();
               si.pop();
               continue;
            }
            level = st.top().first;
            if ((*pv)[idx].isInteger()) {
                val = (*pv)[idx].getInteger();
                sum += val;
                res += level * val;
                continue;
            }
            
            st.push(make_pair(level + 1, &((*pv)[idx].getList())));
            si.push(0);
            max_depth = max(max_depth, (int)st.size());
        }
        res = sum * (max_depth + 1) - res;
        
        return res;
    }
};
