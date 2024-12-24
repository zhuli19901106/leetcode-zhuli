# easy
# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        ai = []
        for i, ch in enumerate(S):
            if ch == C:
                ai.append(i)
        res = []
        m = len(ai)
        for j in range(0, ai[0]):
            res.append(ai[0] - j)
        for i in range(m - 1):
            for j in range(ai[i], ai[i + 1]):
                res.append(min(j - ai[i], ai[i + 1] - j))
        for j in range(ai[m - 1], n):
            res.append(j - ai[m - 1])
        return res
