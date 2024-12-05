# https://leetcode.com/problems/design-neighbor-sum-service/
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.g = [grid[i][:] for i in range(self.n)]
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[self.g[i][j]] = i * self.n + j

    def adjacentSum(self, value: int) -> int:
        idx = self.pos[value]
        i, j = idx // self.n, idx % self.n
        return self.getElement(i - 1, j) + self.getElement(i + 1, j) + \
            self.getElement(i, j - 1) + self.getElement(i, j + 1)

    def diagonalSum(self, value: int) -> int:
        idx = self.pos[value]
        i, j = idx // self.n, idx % self.n
        return self.getElement(i - 1, j - 1) + self.getElement(i + 1, j + 1) + \
            self.getElement(i + 1, j - 1) + self.getElement(i - 1, j + 1)

    def getElement(self, i, j):
        if i >= 0 and i <= self.n - 1 and j >= 0 and j <= self.n - 1:
            return self.g[i][j]
        else:
            return 0

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)