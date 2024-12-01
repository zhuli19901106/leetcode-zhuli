# https://leetcode.com/problems/faulty-keyboard/
class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for c in s:
            if c == 'i':
                res = res[::-1]
            else:
                res.append(c)
        res = ''.join(res)
        return res
