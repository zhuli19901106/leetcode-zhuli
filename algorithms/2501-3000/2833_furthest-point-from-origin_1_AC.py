# https://leetcode.com/problems/furthest-point-from-origin/
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        nl, nr, n_ = 0, 0, 0
        for c in moves:
            if c == 'L':
                nl += 1
            elif c == 'R':
                nr += 1
            else:
                n_ += 1
        return abs(nl - nr) + n_
