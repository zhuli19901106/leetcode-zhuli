# https://leetcode.com/problems/number-of-matching-subsequences/
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def isSub(s, t):
            ls = len(s)
            lt = len(t)
            i = j = 0
            while i < ls and j < lt:
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == lt

        res = 0
        mw = {}
        for w in words:
            if w in mw:
                mw[w] += 1
            else:
                mw[w] = 1
        for w in mw:
            if isSub(S, w):
                res += mw[w]
        return res
