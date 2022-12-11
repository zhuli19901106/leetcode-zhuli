# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        n = len(dictionary[0])
        for q in queries:
            cc = 0
            found = False
            for w in dictionary:
                df = 0
                for i in range(n):
                    if q[i] != w[i]:
                        df += 1
                if df <= 2:
                    found = True
                    break
            if found:
                res.append(q)

        return res
