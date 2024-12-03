# https://leetcode.com/problems/find-missing-and-repeated-values/
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        st = set()
        n = len(grid)

        a, b = -1, -1
        sm = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in st:
                    a = grid[i][j]
                st.add(grid[i][j])
                sm += grid[i][j]
        sm0 = (n * n) * (n * n + 1) // 2
        b = sm0 - sm + a

        return [a, b]
