# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# smooth

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        a = matrix
        n, m = len(a), len(a[0])
        pref_sm = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pref_sm[i + 1][j + 1] = pref_sm[i + 1][j] + pref_sm[i][j + 1] + \
                    a[i][j] - pref_sm[i][j]

    
        res = 0
        for i1 in range(n):
            for i2 in range(i1, n):
                cur = [0 for j in range(m)]
                for j in range(m):
                    cur[j] = pref_sm[i2 + 1][j + 1] + pref_sm[i1][j] - \
                        pref_sm[i2 + 1][j] - pref_sm[i1][j + 1]
                res += self.countTarget(cur, target)

        return res

    def countTarget(self, a, target):
        res = 0

        pref = [0]
        mm = {0: 1}
        sm = 0
        for x in a:
            sm += x
            if sm - target in mm:
                res += mm[sm - target]
            if sm in mm:
                mm[sm] += 1
            else:
                mm[sm] = 1

        return res
