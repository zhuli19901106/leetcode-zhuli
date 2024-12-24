# easy
# https://leetcode.com/problems/distribute-candies-among-children-i/
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(max(0, n - 2 * limit), limit + 1):
            if i > n:
                break
            for j in range(max(0, n - i - limit), limit + 1):
                if i + j > n:
                    break
                res += 1
        return res
