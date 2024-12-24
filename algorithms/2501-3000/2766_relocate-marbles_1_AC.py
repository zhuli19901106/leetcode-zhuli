# medium
# https://leetcode.com/problems/relocate-marbles/
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        balls = {}
        for x in nums:
            if not x in balls:
                balls[x] = 0
            balls[x] += 1

        m = len(moveFrom)
        for i in range(m):
            p1, p2 = moveFrom[i], moveTo[i]
            if p1 == p2:
                continue

            if not p1 in balls:
                continue

            cc = balls[p1]

            if not p2 in balls:
                balls[p2] = 0
            balls[p2] += cc
            del balls[p1]

        return sorted(balls.keys())
