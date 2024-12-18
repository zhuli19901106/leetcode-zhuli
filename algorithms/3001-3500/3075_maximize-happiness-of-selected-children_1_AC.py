# https://leetcode.com/problems/maximize-happiness-of-selected-children/
# why is this medium?
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            res += max(happiness[i] - i, 0)
        return res
