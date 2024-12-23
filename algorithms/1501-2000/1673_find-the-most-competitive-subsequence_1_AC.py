# https://leetcode.com/problems/find-the-most-competitive-subsequence/
# got me stuck for over 20 minutes and finally got it
# this is almost a hard medium
# even after hearing "monotonic stack", still took me a while to work it out
# try this, 2433509617834
# [24] [33]
# [2335] []
# [233] [0]
# [23] [09]
# [2] [096]
# [09] [61]
# [06] [17]
# [0178] []
# [017] [3]
# [0134] []

from collections import deque

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return [min(nums)]

        st = []
        q = deque()

        for i in range(k):
            x = nums[i]
            if len(q) == 0 and (len(st) == 0 or x >= st[-1]):
                st.append(x)
            else:
                q.append(x)

        n = len(nums)
        for i in range(k, n):
            x = nums[i]
            q.append(x)

            # pop the bigger one
            if st[-1] > q[0]:
                st.pop()
            else:
                q.popleft()

            # make sure st is always increasing
            while len(q) > 0 and (len(st) == 0 or q[0] >= st[-1]):
                st.append(q.popleft())

        while len(q) > 0:
            st.append(q.popleft())
        return st
