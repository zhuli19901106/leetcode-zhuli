# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(s):
            res = []
            for c in s:
                if c == '#':
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(c)
            return ''.join(res)

        return process(S) == process(T)
