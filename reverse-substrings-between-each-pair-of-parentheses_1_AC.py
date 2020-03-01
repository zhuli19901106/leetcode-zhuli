# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        a = []
        st = [[]]
        for c in s:
            if c == '(':
                st.append([])
                st[-1].append(c)
            elif c == ')':
                st[-1].append(c)
                tmp = st.pop()
                while len(tmp) > 0:
                    st[-1].append(tmp.pop())
            else:
                st[-1].append(c)
        return ''.join([c for c in st.pop() if (c != '(' and c != ')')])
