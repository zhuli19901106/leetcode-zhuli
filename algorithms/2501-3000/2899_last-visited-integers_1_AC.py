# https://leetcode.com/problems/last-visited-integers/
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        res = []
        n = len(nums)
        j = -2
        for x in nums:
            if x > 0:
                j = -2
                seen.append(x)
                continue

            if j == -2:
                j = len(seen) - 1

            if j >= 0:
                res.append(seen[j])
                j -= 1
            else:
                res.append(-1)

        return res
