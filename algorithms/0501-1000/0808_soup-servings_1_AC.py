# medium
# https://leetcode.com/problems/soup-servings/
# https://leetcode.com/problems/soup-servings/discuss/537584/808-Soup-Servings-Py-All-in-One-by-Talse
# man... I'm simply served on this one
class Solution:
    def __init__(self):
        self.dp = {}

    def soupServings(self, N: int) -> float:
        # why can't I come up with the clipping here?
        MAXN = 10000
        if N > MAXN:
            return 1

        def serve(x, y):
            if (x, y) in self.dp:
                return self.dp[(x, y)]
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1
            if y <= 0:
                return 0
            self.dp[(x, y)] = (\
                serve(x - 4, y) +\
                serve(x - 3, y - 1) +\
                serve(x - 2, y - 2) +\
                serve(x - 1, y - 3)) / 4
            return self.dp[(x, y)]

        # downscale to save memory
        return serve((N + 24) // 25, (N + 24) // 25)
