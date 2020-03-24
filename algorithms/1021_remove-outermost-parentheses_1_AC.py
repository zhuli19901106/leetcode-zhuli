# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        cnt = 0
        i = 0
        j = 0
        ls = len(S)
        while j < ls:
            if S[j] == '(':
                cnt += 1
            elif S[j] == ')':
                cnt -= 1
            j += 1
            if cnt == 0:
                res += S[i + 1: j - 1]
                i = j
        return res
