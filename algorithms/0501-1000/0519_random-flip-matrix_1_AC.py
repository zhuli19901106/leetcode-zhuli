# medium
# https://leetcode.com/problems/random-flip-matrix/
# https://en.wikipedia.org/wiki/Linear_congruential_generator
# a good example of python yield
# without theoretical knowledge of LCG, this can be tough
from math import log2
from random import randint

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.nr = n_rows
        self.nc = n_cols
        self.it = self.sample(self.nr * self.nc)

    def flip(self) -> List[int]:
        idx = next(self.it)
        return [idx // self.nc, idx % self.nc]

    def reset(self) -> None:
        self.it = self.sample(self.nr * self.nc)

    def sample(self, n):
        bl = int(floor(log2(n))) + 1
        m2 = 1 << bl
        idx = randint(1, n - 1)
        for i in range(n):
            while True:
                idx = (idx * 5 + 1) % m2
                if idx < n:
                    break
            yield idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()