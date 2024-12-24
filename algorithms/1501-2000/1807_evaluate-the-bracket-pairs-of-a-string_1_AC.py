# medium
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# 1AC, templating
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mm = {}
        for k, v in knowledge:
            mm[k] = v

        n = len(s)
        i = 0
        res = []
        while i < n:
            if s[i] != '(':
                res.append(s[i])
                i += 1
                continue
            i += 1
            key = []
            while i < n and s[i] != ')':
                key.append(s[i])
                i += 1
            key = ''.join(key)
            res.append(mm[key] if key in mm else '?')
            i += 1

        res = ''.join(res)
        return res
