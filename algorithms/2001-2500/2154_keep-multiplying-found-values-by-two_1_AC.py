# https://leetcode.com/problems/keep-multiplying-found-values-by-two/
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        st = set(nums)
        while original in st:
            original *= 2
        return original
