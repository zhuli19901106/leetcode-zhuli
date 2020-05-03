# https://leetcode.com/problems/string-matching-in-an-array/
# 1AC, brute-force match
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ws = words
        ws.sort(key=lambda s: len(s))
        n = len(ws)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                if ws[j].find(ws[i]) != -1:
                    res.append(ws[i])
                    break
        return res
