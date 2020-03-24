# https://leetcode.com/problems/advantage-shuffle/
# 1AC, Tian Ji's horse racing
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = sorted([(x, i) for i, x in enumerate(A)])
        b = sorted([(x, i) for i, x in enumerate(B)])
        n = len(a)

        i = 0
        j = 0
        k = n - 1
        res = [0 for i in range(n)]
        while i < n:
            if a[i][0] > b[j][0]:
                res[b[j][1]] = a[i][0]
                i += 1
                j += 1
            else:
                res[b[k][1]] = a[i][0]
                i += 1
                k -= 1
        return res
