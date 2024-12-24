# hard
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = []
        st = []
        for x in reversed(heights):
            cur = 0

            while len(st) > 0 and st[-1] <= x:
                cur += 1
                st.pop()

            if len(st) > 0:
                cur += 1

            res.append(cur)
            st.append(x)
        res = res[::-1]

        return res
