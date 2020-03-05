# https://leetcode.com/problems/corporate-flight-bookings/
# better yet, use postfix sum to accumulate the changes
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for i in range(n)]
        for i, j, val in bookings:
            if i > 1:
                res[i - 2] -= val
            res[j - 1] += val
        for i in range(n - 1, 0, -1):
            res[i - 1] += res[i]
        return res
