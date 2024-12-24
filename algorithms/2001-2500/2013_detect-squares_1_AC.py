# medium
# https://leetcode.com/problems/detect-squares/
# just BF, it's actually easier than I supposed
class DetectSquares:

    def __init__(self):
        # the count of points at each position
        self.mp = {}

    def add(self, point: List[int]) -> None:
        mp = self.mp

        x1, y1 = point
        if not (x1, y1) in mp:
            mp[(x1, y1)] = 0
        mp[(x1, y1)] += 1

    def count(self, point: List[int]) -> int:
        mp = self.mp

        x1, y1 = point
        res = 0
        for x2, y2 in mp:
            if (x1, y1) == (x2, y2):
                continue

            # pick two diagonal points
            if x1 == x2 or y1 == y2:
                continue

            # must be a square
            if not abs(x2 - x1) == abs(y2 - y1):
                continue

            # look for the other two
            if not ((x1, y2) in mp and (x2, y1) in mp):
                continue

            c1, c2 = 1, mp[(x2, y2)]
            c3, c4 = mp[(x1, y2)], mp[(x2, y1)]
            res += c1 * c2 * c3 * c4

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)