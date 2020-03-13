# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# left max, right min
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        a = A
        n = len(a)
        ml = [0 for i in range(n)]
        ml[0] = a[0]
        for i in range(1, n):
            ml[i] = max(ml[i - 1], a[i])

        mr = [0 for i in range(n)]
        mr[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            mr[i] = min(mr[i + 1], a[i])
        for i in range(n - 1):
            if ml[i] <= mr[i + 1]:
                return i + 1
        return -1
