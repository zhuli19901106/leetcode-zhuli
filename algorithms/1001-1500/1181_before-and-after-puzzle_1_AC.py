# https://leetcode.com/problems/before-and-after-puzzle/
# 1AC, O(n^2) brute-force solution
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        ms = {}
        me = {}
        atk = []
        for i, s in enumerate(phrases):
            tk = s.strip().split()
            atk.append(tk)
            start, end = tk[0], tk[-1]
            if not start in ms:
                ms[start] = []
            ms[start].append(i)
            if not end in me:
                me[end] = []
            me[end].append(i)

        res = set()
        for end in me:
            if not end in ms:
                continue
            for i in me[end]:
                for j in ms[end]:
                    if i == j:
                        continue
                    res.add(' '.join(atk[i][:-1] + atk[j]))
        return sorted(res)
