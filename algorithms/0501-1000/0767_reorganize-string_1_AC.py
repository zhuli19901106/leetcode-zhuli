# medium
# https://leetcode.com/problems/reorganize-string/
# tricky and tiresome, but not difficult
class Solution:
    def reorganizeString(self, S: str) -> str:
        mc = {}
        for c in S:
            if c in mc:
                mc[c] += 1
            else:
                mc[c] = 1
        mc = list(mc.items())
        mc.sort(key=lambda x: -x[1])

        n = len(S)
        if mc[0][1] > (n + 1) // 2:
            return ''

        i = 0
        j = 0
        res = ['#' for i in range(n)]

        while i < n:
            c, nk = mc[j]
            k = 0
            while i < n and k < nk:
                res[i] = c
                i += 2
                k += 1
            if k == nk:
                j += 1

        i = 1
        if k < nk:
            j += 1
        while k < nk:
            res[i] = c
            i += 2
            k += 1

        i = n - 1 if n % 2 == 0 else n - 2
        nc = len(mc)
        while i >= 0 and j < nc:
            c, nk = mc[j]
            k = 0
            while i >= 0 and k < nk:
                res[i] = c
                i -= 2
                k += 1

            if k == nk:
                j += 1

        return ''.join(res)
