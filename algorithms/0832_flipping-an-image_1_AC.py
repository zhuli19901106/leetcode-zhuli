# https://leetcode.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 - x for x in row[::-1]] for row in A]
