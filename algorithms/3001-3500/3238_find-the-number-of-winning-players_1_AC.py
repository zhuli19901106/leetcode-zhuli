# easy
# https://leetcode.com/problems/find-the-number-of-winning-players/
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        mm = [{} for i in range(n)]
        for x, y in pick:
            if not y in mm[x]:
                mm[x][y] = 1
            else:
                mm[x][y] += 1

        res = 0
        for i in range(n):
            if len(mm[i]) == 0:
                continue
            if max(mm[i].values()) > i:
                res += 1
        return res
