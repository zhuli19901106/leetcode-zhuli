# medium
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
# use a sorted set
# don't bother recording intervals, too much trouble
from sortedcontainers import SortedSet

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # separate entering and leaving events
        a = []
        for i, tp in enumerate(times):
            x, y = tp
            # 1 for enter and 0 for leave
            a.append((x, 1, i))
            a.append((y, 0, i))
        a.sort()

        n = len(times)
        seats = SortedSet()
        for i in range(n):
            seats.add(i)

        res = [-1 for i in range(n)]
        for t, ev, idx in a:
            # enter
            if ev == 1:
                # enough seats are guaranteed, always
                x = seats[0]
                seats.remove(x)
                res[idx] = x
            # leave
            else:
                x = res[idx]
                seats.add(x)
        return res[targetFriend]
