# easy
# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = dict([(order[i], chr(ord('a') + i)) for i in range(26)])
        def transform(s):
            return ''.join([m[c] for c in s])

        aw = [transform(w) for w in words]
        nw = len(aw)
        for i in range(nw - 1):
            if aw[i] > aw[i + 1]:
                return False
        return True
