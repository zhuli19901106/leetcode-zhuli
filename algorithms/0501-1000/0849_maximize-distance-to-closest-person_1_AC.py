# https://leetcode.com/problems/maximize-distance-to-closest-person/
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        i = j = 0
        res = 0
        while i < n:
            if j < n and seats[i] == seats[j]:
                j += 1
            else:
                if seats[i] != 0:
                    i = j
                    continue
                if i == 0 or j == n:
                    res = max(res, j - i)
                else:
                    res = max(res, (j - i + 1) // 2)
                i = j
        return res
