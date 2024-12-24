# medium
# https://leetcode.com/problems/moving-stones-until-consecutive/
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        d1 = b - a - 1
        d2 = c - b - 1
        max_move = d1 + d2
        min_move = 0
        if d1 > 0:
            min_move += 1
        if d2 > 0:
            min_move += 1
        if d1 == 1 or d2 == 1:
            min_move = 1
        return [min_move, max_move]
