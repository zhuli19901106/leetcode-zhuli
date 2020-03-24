# https://leetcode.com/problems/expressive-words/
# 1AC
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def rle(s):
            n = len(s)
            i = 0
            res = []
            while i < n:
                j = i + 1
                while j < n and s[i] == s[j]:
                    j += 1
                res.append((s[i], j - i))
                i = j
            return res

        rs = rle(S)
        ns = len(rs)
        res = 0
        for w in words:
            rw = rle(w)
            if len(rw) != ns:
                continue
            i = 0
            while i < ns:
                if rw[i][0] != rs[i][0]:
                    break
                if rw[i][1] > rs[i][1]:
                    break
                if rs[i][1] < 3 and rw[i][1] != rs[i][1]:
                    break
                i += 1
            if i == ns:
                res += 1
        return res
