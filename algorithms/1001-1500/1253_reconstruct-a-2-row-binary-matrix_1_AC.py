# medium
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        a = [[-1 for j in range(n)] for i in range(2)]
        n1 = 0
        for i, x in enumerate(colsum):
            if x == 2:
                upper -= 1
                lower -= 1
                a[0][i] = a[1][i] = 1
            elif x == 1:
                n1 += 1
            elif x == 0:
                a[0][i] = a[1][i] = 0
        if upper < 0 or lower < 0 or n1 != upper + lower:
            return []
        for i in range(n):
            if a[0][i] != -1:
                continue
            if upper > 0:
                a[0][i] = 1
                a[1][i] = 0
                upper -= 1
            else:
                a[0][i] = 0
                a[1][i] = 1
                lower -= 1
        return a
