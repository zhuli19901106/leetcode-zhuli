# easy
# https://leetcode.com/problems/row-with-maximum-ones/
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_cc, max_i = 0, 0
        n= len(mat)
        for i in range(n):
            cc = sum(mat[i])
            if cc > max_cc:
                max_cc, max_i = cc, i
        return [max_i, max_cc]
