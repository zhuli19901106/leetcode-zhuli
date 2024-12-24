# medium
# https://leetcode.com/problems/generate-random-point-in-a-circle/
# got really annoyed with precision problem from radial sampling
from random import uniform

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.cx = x_center
        self.cy = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x = uniform(self.cx - self.r, self.cx + self.r)
            y = uniform(self.cy - self.r, self.cy + self.r)
            # precision problem
            if (x - self.cx) ** 2 + (y - self.cy) ** 2 < self.r ** 2:
                break
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()