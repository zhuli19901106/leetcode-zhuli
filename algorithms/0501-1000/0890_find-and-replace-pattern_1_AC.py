# https://leetcode.com/problems/find-and-replace-pattern/
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for w in words:
            if Solution.isSamePerm(w, pattern):
                res.append(w)
        return res

    @staticmethod
    def getPerm(s):
        m = {}
        res = []
        i = 0
        for c in s:
            if not c in m:
                m[c] = i
                i += 1
            res.append(m[c])
        return res

    @staticmethod
    def isSamePerm(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            return False
        a1 = Solution.getPerm(s1)
        a2 = Solution.getPerm(s2)
        return a1 == a2
