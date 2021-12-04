# https://leetcode.com/problems/sorting-the-sentence/
# 1AC

class Solution:
    def sortSentence(self, s: str) -> str:
        ws = s.split()
        res = [0 for _ in range(len(ws))]
        for w_i in ws:
            w = w_i[:-1]
            i = int(w_i[-1]) - 1
            res[i] = w
        return ' '.join(res)
