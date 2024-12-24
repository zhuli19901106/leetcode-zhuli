# medium
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/
# the idea is a bit tricky I think
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        INT_MAX = 2 ** 31 - 1

        a = sorted(stones)
        n = len(a)
        d1 = a[1] - a[0] - 1
        d2 = a[n - 1] - a[n - 2] - 1
        ds = a[n - 1] - a[0] - 1 - (n - 2)
        max_move = ds - min(d1, d2)

        i = 0
        j = 1
        min_move = INT_MAX
        while i < n:
            while j < n and a[j] < a[i] + n - 1:
                j += 1
            if j == n:
                break
            if a[j]== a[i] + n - 1:
                cnt = n - (j - i + 1)
            else:
                # special case
                cnt = max(n - (j - i), 2)
            min_move = min(min_move, cnt)
            i += 1

        return [min_move, max_move]
