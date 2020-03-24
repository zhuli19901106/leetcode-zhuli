# https://leetcode.com/problems/print-words-vertically/
class Solution:
    def printVertically(self, s: str) -> List[str]:
        ws = s.split()
        n = max([len(x) for x in ws])
        m = len(ws)
        a = [[' ' for j in range(m)] for i in range(n)]
        for j, w in enumerate(ws):
            for i, c in enumerate(w):
                a[i][j] = c
        res = [(''.join(x)).rstrip() for x in a]
        return res
