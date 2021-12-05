# https://leetcode.com/problems/convert-1d-array-into-2d-array/
# 1AC

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        no = len(original)
        if m * n != no:
            return []
        res = []
        for i in range(m):
            res.append([])
            for j in range(n):
                res[-1].append(original[i * n + j])
        return res
