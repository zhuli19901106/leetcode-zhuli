# https://leetcode.com/problems/stone-game-vi/
# I hate these games, seriously.
# sort it, but I can't prove why it works.
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        sm = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        sm.sort(reverse=True)

        p = [0, 0]
        f = 0
        for _, i in sm:
            if f == 0:
                p[f] += aliceValues[i]
            else:
                p[f] += bobValues[i]
            f = 1 - f
        return 1 if p[0] > p[1] else -1 if p[0] < p[1] else 0
