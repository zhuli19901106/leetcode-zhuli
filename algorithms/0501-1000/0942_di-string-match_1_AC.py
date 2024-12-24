# easy
# https://leetcode.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S) + 1
        i = 0
        j = n - 1
        res = []
        for c in S:
            if c == 'I':
                res.append(i)
                i += 1
            elif c == 'D':
                res.append(j)
                j -= 1
        res.append(i)
        i += 1
        return res
