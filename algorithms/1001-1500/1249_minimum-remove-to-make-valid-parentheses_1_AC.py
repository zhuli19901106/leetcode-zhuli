# medium
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# think it over and code clean
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mp = {}
        st = []
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if len(st) == 0:
                    continue
                mp[i] = st[-1]
                mp[st[-1]] = i
                st.pop()
        res = []
        for i, c in enumerate(s):
            if (c == '(' or c == ')') and not i in mp:
                continue
            res.append(c)
        return ''.join(res)
