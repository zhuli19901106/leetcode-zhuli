# easy
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# 1AC
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        res = []
        for c in candies:
            res.append(c + extraCandies >= max_c)
        return res
