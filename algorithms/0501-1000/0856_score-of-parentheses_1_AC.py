# https://leetcode.com/problems/score-of-parentheses/
# Runtime: 20 ms, faster than 95.65% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Score of Parentheses.
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st = [0]
        for c in S:
            if c == '(':
                st.append(0)
            elif c == ')':
                if st[-1 ] == 0:
                    st.pop()
                    st[-1] += 1
                else:
                    sc = st.pop()
                    st[-1] += sc * 2
        return st.pop()
