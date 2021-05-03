# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
# 1AC, actually easier than submatrix sum
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        mx = [[0 for j in range(m + 1)] for i in range(n + 1)]
        arr = []
        for i in range(n):
            for j in range(m):
                mx[i + 1][j + 1] ^= mx[i + 1][j]
                mx[i + 1][j + 1] ^= mx[i][j + 1]
                mx[i + 1][j + 1] ^= mx[i][j]
                mx[i + 1][j + 1] ^= matrix[i][j]
                arr.append(mx[i + 1][j + 1])
        arr.sort()
        return arr[n * m - k]
