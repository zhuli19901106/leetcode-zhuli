# medium
# https://leetcode.com/problems/longest-square-streak-in-an-array/
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        st = set(nums)
        a = sorted(st)

        res = -1
        for x in a:
            # already visited
            if not x in st:
                continue

            cc = 0
            while x in st:
                st.remove(x)
                cc += 1
                x *= x
            if cc >= 2 and res < cc:
                res = cc
        return res
