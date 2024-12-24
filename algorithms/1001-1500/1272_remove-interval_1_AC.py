# medium
# https://leetcode.com/problems/remove-interval/
# 1AC, well, I implemented a harder version because I misunerstood the problem
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ai = intervals
        ni = len(ai)
        # it's just a single one
        at = [toBeRemoved]
        at.sort()
        nt = len(at)

        i = j = 0
        res = []
        while i < ni:
            # no more remove
            if j == nt:
                res.append(ai[i])
                i += 1
                continue
            # remover too far left
            if ai[i][0] >= at[j][1]:
                j += 1
                continue
            # remover too far right
            if ai[i][1] <= at[j][0]:
                res.append(ai[i])
                i += 1
                continue

            if ai[i][0] < at[j][0]:
                res.append([ai[i][0], at[j][0]])
            if ai[i][1] > at[j][1]:
                ai[i][0] = at[j][1]
                j += 1
            elif ai[i][1] < at[j][1]:
                at[j][0] = ai[i][1]
                i += 1
            else:
                i += 1
                j += 1
        return res
