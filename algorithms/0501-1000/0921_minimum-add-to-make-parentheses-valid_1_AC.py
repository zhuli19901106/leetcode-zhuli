# medium
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        cnt = 0
        for c in S:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt > 0:
                    cnt -= 1
                else:
                    res += 1
        res += cnt
        cnt = 0
        return res
