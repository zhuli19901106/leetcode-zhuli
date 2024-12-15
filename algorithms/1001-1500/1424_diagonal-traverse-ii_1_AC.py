# https://leetcode.com/problems/diagonal-traverse-ii/
# careful, it's not a matrix, could be sparse
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ai = []
        for i, r in enumerate(nums):
            ai += [(i + j, j, i) for j in range(len(r))]
        ai.sort()

        res = [nums[i][j] for _, j, i in ai]
        return res
