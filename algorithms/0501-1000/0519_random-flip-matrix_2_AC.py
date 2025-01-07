# medium
# https://leetcode.com/problems/random-flip-matrix/
# Fisher-Yates shuffle
# slower but much simpler to understand than LCG
from random import randint

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.nr = n_rows
        self.nc = n_cols
        self.it = self.sample()

    def flip(self) -> List[int]:
        idx = next(self.it)
        return [idx // self.nc, idx % self.nc]

    def reset(self) -> None:
        self.it = self.sample()

    def sample(self):
        nr = self.nr
        nc = self.nc

        ro = list(range(nr))
        for i in range(nr - 1, -1, -1):
            ri = randint(0, i)
            ro[ri], ro[i] = ro[i], ro[ri]
            rv = ro[i]

            co = list(range(nc))
            for j in range(nc - 1, -1, -1):
                cj = randint(0, j)
                co[cj], co[j] = co[j], co[cj]
                cv = co[j]

                yield rv * nc + cv

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()