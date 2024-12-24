# easy
# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        a = [sorted(s) for s in A]
        n = len(a)
        if n == 0:
            return a
        res = a[0]
        i = 1
        while i < n:
            res = self.common(res, a[i])
            i += 1
        return list(res)

    def common(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        i1 = 0
        i2 = 0
        res = []
        while i1 < n1 and i2 < n2:
            if s1[i1] < s2[i2]:                
                i1 += 1
            elif s1[i1] > s2[i2]:
                i2 += 1
            else:
                res.append(s1[i1])
                i1 += 1
                i2 += 1
        return ''.join(res)
