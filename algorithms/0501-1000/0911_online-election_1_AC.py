# medium
# https://leetcode.com/problems/online-election/
# preprocess and binary search
from bisect import bisect_right

class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        INT_MIN = -(2 ** 31)
        max_val = (-1, INT_MIN)
        m = {}

        amx = []
        for i, x in enumerate(persons):
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
            if m[x] >= max_val[1]:
                max_val = (x, m[x])
            amx.append(max_val)
        self.at = times
        self.amx = amx

    def q(self, t: int) -> int:
        n = len(self.at)
        i = bisect_right(self.at, t) - 1
        if i < 0:
            return -1
        return self.amx[i][0]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)