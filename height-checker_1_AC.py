# https://leetcode.com/problems/height-checker/
# this problem is not clearly worded
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                count += 1
        return count
