# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# got overcooked

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # filter relevant intervals
        ar = [(x, y) for x, y in ranges]
        ar.sort()

        # merge intervals
        ar_merge = []
        for x, y in ar:
            if len(ar_merge) == 0:
                ar_merge.append((x, y))
                continue
            x0, y0 = ar_merge[-1]
            if x > y0 + 1:
                ar_merge.append((x, y))
                continue
            ar_merge[-1] = (min(x0, x), max(y0, y))

        for x, y in ar_merge:
            if x <= left and y >= right:
                return True
        return False
