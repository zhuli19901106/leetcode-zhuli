# medium
# https://leetcode.com/problems/magnetic-force-between-two-balls/
# first reaction was DP, but not viable due to scale and complexity

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        a = sorted(position)
        n = len(a)

        ll, rr = 1, a[-1] - a[0] + 1
        while rr - ll > 1:
            mm = ll + (rr - ll) // 2

            x = mm
            i, j = 1, 1
            last_i = 0
            ok = False
            while True:
                if i >= n or j >= m:
                    break
                if a[i] - a[last_i] >= x:
                    last_i = i
                    j += 1
                i += 1

            if j >= m:
                ok = True
            if ok:
                ll = mm
            else:
                rr = mm

        return ll
