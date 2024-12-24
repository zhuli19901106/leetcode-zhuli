# medium
# https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def countChars(s):
            mm = {}
            for c in s:
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1

            return mm

        m1 = countChars(word1)
        m2 = countChars(word2)
        av1 = sorted(m1.values())
        av2 = sorted(m2.values())

        n = len(av1)
        if len(av2) != n:
            return False
        for i in range(n):
            if av1[i] != av2[i]:
                return False

        ak1 = sorted(m1.keys())
        ak2 = sorted(m2.keys())

        n = len(ak1)
        if len(ak2) != n:
            return False
        for i in range(n):
            if ak1[i] != ak2[i]:
                return False

        return True
