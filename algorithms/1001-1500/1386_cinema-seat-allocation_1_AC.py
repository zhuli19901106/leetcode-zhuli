# https://leetcode.com/problems/cinema-seat-allocation/
# precompute by enumerating 1024 possibilities
class Solution:
    def __init__(self):
        m = 10
        # enumerate all 2^10 possibilities
        seat_fam = [0 for i in range(1 << m)]
        for i in range(len(seat_fam)):
            bl = ((i & (0xf << 5)) == 0)
            br = ((i & (0xf << 1)) == 0)
            bm = ((i & (0xf << 3)) == 0)
            res = 0
            if bl:
                res += 1
            if br:
                res += 1
            if res == 0 and bm:
                res += 1
            seat_fam[i] = res
        self.seat_fam = seat_fam

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mm = {}
        for x, y in reservedSeats:
            if not x in mm:
                mm[x] = 0
            mm[x] |= (1 << y - 1)
        # totally empty rows
        res = 2 * (n - len(mm))

        seat_fam = self.seat_fam
        for v in mm.values():
            res += seat_fam[v]
        return res
