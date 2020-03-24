// Don't you think that such problems are a bit too complicated for a technical interview?
// Immutable reference is one hell of a foolish feature in C++.
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
#include <cctype>
#include <stack>
using std::isdigit;
using std::stack;

class Solution {
public:
    NestedInteger deserialize(string s) {
        stack<NestedInteger *> st;
        int ls = s.size();
        int i = 0;
        NestedInteger *item;
        NestedInteger *res;
        while (i < ls) {
            if (s[i] == '[') {
                item =  new NestedInteger();
                if (!st.empty()) {
                    st.top()->getList().push_back(*item);
                    st.push(&(st.top()->getList().back()));
                } else {
                    res = item;
                    st.push(item);
                }
                
            } else if (s[i] == ']') {
                if (st.size() == 1) {
                    res = st.top();
                }
                st.pop();
            } else if (s[i] == '-' || s[i] == '+' || isdigit(s[i])) {
                int sign = 1;
                if (s[i] == '-') {
                    sign = -1;
                    ++i;
                } else if (s[i] == '+') {
                    ++i;
                }
                int val = 0;
                while (i < ls && isdigit(s[i])) {
                    val = val * 10 + (s[i] - '0');
                    ++i;
                }
                item = new NestedInteger(sign * val);
                if (!st.empty()) {
                    st.top()->getList().push_back(*item);
                } else {
                    res = item;
                }
                --i;
            }
            ++i;
        }
        return *res;
    }
};
