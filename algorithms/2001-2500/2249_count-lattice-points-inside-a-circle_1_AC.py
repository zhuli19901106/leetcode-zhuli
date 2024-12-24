# medium
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/
# use binary search to speed up a little
# enumerate everything
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for cx, cy, r in circles:
            res.add((cx, cy))
            for i in range(1, r + 1):
                res.add((cx + i, cy))
                res.add((cx - i, cy))
                res.add((cx, cy + i))
                res.add((cx, cy - i))

            for i in range(1, r + 1):
                ll, rr = 0, r + 1
                while rr - ll > 1:
                    mm = ll + (rr - ll >> 1)
                    if i * i + mm * mm <= r * r:
                        ll = mm
                    else:
                        rr = mm
                for j in range(1, ll + 1):
                    res.add((cx + j, cy + i))
                    res.add((cx - j, cy + i))
                    res.add((cx + j, cy - i))
                    res.add((cx - j, cy - i))

        return len(res)
