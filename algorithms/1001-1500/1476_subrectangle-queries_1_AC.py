# medium
# https://leetcode.com/problems/subrectangle-queries/
# 1AC, nothing more
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.arr = [r[:] for r in rectangle]
        self.n = len(rectangle)
        self.m = len(rectangle[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        a = self.arr
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                a[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.arr[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)