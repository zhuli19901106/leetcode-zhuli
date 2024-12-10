# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/
# should be "easy"
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        n = len(nums)
        idx = [i for i in range(n) if nums[i] == x]

        res = [idx[q - 1] if q <= len(idx) else -1 for q in queries]
        return res
