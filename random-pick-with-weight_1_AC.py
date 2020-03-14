# https://leetcode.com/problems/random-pick-with-weight/
# discrete pdf and cdf
from bisect import bisect_right
from random import randint

class Solution:
    def __init__(self, w: List[int]):
        n = len(w)
        ps = [0]
        for x in w:
            ps.append(ps[-1] + x)
        self.ps = ps

    def pickIndex(self) -> int:
        x = randint(0, self.ps[-1] - 1)
        idx = bisect_right(self.ps, x) - 1
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()