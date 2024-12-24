# medium
# https://leetcode.com/problems/bold-words-in-string/
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        b = [False for i in range(len(S))]
        for w in words:
            i = 0
            nw = len(w)
            while True:
                j = S.find(w, i)
                if j == -1:
                    break
                for k in range(nw):
                    b[j + k] = True
                i = j + 1
        res = []
        ns = len(S)
        for i, c in enumerate(S):
            if not b[i]:
                res.append(c)
                continue
            if i == 0 or not b[i - 1]:
                res.append('<b>')
            res.append(c)
            if (i == ns - 1 or not b[i + 1]):
                res.append('</b>')
        return ''.join(res)
