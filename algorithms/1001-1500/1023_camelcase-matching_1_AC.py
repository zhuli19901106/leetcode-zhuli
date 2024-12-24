# medium
# https://leetcode.com/problems/camelcase-matching/
# 1AC
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(s, p):
            ns = len(s)
            np = len(p)
            i = j = 0
            while i < ns or j < np:
                if i == ns:
                    return False
                if j == np:
                    if s[i].islower():
                        i += 1
                        continue
                    else:
                        return False
                if s[i] == p[j]:
                    i += 1
                    j += 1
                elif s[i].islower():
                    i += 1
                else:
                    return False
            return True

        res = []
        for q in queries:
            res.append(match(q, pattern))
        return res
