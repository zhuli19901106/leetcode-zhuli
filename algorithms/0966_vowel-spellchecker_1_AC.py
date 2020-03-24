# https://leetcode.com/problems/vowel-spellchecker/
# 1AC
# Runtime: 180 ms, faster than 91.44% of Python3 online submissions for Vowel Spellchecker.
# Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Vowel Spellchecker.
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vw = set('aeiou')
        me = set(wordlist)

        mc = {}
        for w in wordlist:
            wl = w.lower()
            if not wl in mc:
                mc[wl] = w

        def getPat(w):
            aw = list(w.lower())
            for i, c in enumerate(aw):
                if c in vw:
                    aw[i] = '*'
            return ''.join(aw)

        mv = {}
        for w in wordlist:
            wv = getPat(w)
            if not wv in mv:
                mv[wv] = w

        res = []
        for q in queries:
            if q in me:
                res.append(q)
                continue
            q1 = q.lower()
            if q1 in mc:
                res.append(mc[q1])
                continue
            q1 = getPat(q)
            if q1 in mv:
                res.append(mv[q1])
                continue
            res.append('')
        return res
