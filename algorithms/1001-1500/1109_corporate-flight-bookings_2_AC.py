# https://leetcode.com/problems/corporate-flight-bookings/
# sort and calculate prefix sum
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = []
        for b in bookings:
            a.append((b[0] - 1, -b[2]))
            a.append((b[1], b[2]))
        a.sort()
        na = len(a)
        ps = [0 for i in range(na + 1)]
        for i in range(na):
            ps[i + 1] = ps[i] + a[i][1]

        j = 0
        res = []
        for i in range(1, n + 1):
            while j < na and a[j][0] < i:
                j += 1
            res.append(ps[na] - ps[j])
        return res
