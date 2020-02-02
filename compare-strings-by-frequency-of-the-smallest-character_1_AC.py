# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq(w):
            return w.count(sorted(w)[0])

        res = []
        fws = sorted([freq(w) for w in words])
        n = len(fws)
        for q in queries:
            fq = freq(q)
            i = bisect_right(fws, fq)
            res.append(n - i)
        return res
