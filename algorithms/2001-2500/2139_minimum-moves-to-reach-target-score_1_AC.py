# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target != 1 and maxDoubles > 0:
            if target & 1 == 0 and maxDoubles > 0:
                maxDoubles -= 1
                target >>= 1
            else:
                target -= 1
            res += 1

        res += target - 1
        return res
