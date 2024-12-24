# easy
# https://leetcode.com/problems/play-with-chips/
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        n = len(chips)
        odd = len([x for x in chips if x % 2 == 1])
        even = n - odd
        return min(odd, even)
