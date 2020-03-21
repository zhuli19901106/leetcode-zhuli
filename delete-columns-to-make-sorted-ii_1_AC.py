# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# compare column by column
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        a = A
        n = len(a)
        if n == 0:
            return 0
        m = len(a[0])
        if m == 0:
            return 0

        res = 0
        ari = [list(range(n - 1))]
        for i in range(m):
            ri = ari[-1]
            j = 0
            nri = len(ri)
            ri1 = []
            while j < nri:
                if a[ri[j]][i] > a[ri[j] + 1][i]:
                    res += 1
                    break
                elif a[ri[j]][i] == a[ri[j] + 1][i]:
                    ri1.append(ri[j])
                j += 1
            if j < nri:
                continue
            elif len(ri1) == 0:
                break
            else:
                ari.append(ri1)

        return res
