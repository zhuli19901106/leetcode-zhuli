# medium
# https://leetcode.com/problems/finding-the-users-active-minutes/
# 1AC, for a simple question, the description is unnecessarily convoluted
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        stats = {}
        for u, t in logs:
            if not u in stats:
                stats[u] = set()
            stats[u].add(t)

        res = [0 for _ in range(k)]
        for u, st in stats.items():
            uam = len(st)
            if uam >= 1 and uam <= k:
                res[uam - 1] += 1
        return res
