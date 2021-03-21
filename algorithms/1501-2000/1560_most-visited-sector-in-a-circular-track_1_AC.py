# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
# 1AC, can be optimized by BIT, but don't wanna bother for an easy one
# boundary description is confusing
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        cc = [0 for _ in range(n + 1)]
        i = 1
        m = len(rounds) - 1
        for j in range(m):
            x, y = rounds[j], rounds[j + 1]
            if x < y:
                for k in range(x, y):
                    cc[k] += 1
            else:
                for k in range(x, n + 1):
                    cc[k] += 1
                for k in range(1, y):
                    cc[k] += 1
        cc[rounds[-1]] += 1

        max_cc = max(cc)
        res = [i for i in range(1, n + 1) if cc[i] == max_cc]
        return res
